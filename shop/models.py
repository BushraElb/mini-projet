
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Nom")
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True, null=True, verbose_name="Image")
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name="Catégorie parente"
    )
    is_main_category = models.BooleanField(default=False, verbose_name="Catégorie principale")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('order', 'name',)
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
        unique_together = [['slug', 'parent']]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            
            while Category.objects.filter(slug=slug, parent=self.parent).exclude(pk=self.pk if self.pk else None).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    
    def get_subcategories(self):
        """Retourne les sous-catégories"""
        return self.children.all()


class Product(models.Model):
    """Modèle pour les produits"""
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name="Catégorie"
    )
    name = models.CharField(max_length=200, db_index=True, verbose_name="Nom")
    slug = models.SlugField(max_length=200, db_index=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Image")
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False, verbose_name="Produit populaire")
    display_order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ('display_order', '-created_at',)
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

