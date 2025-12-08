"""
Modèles pour l'application shop
"""
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Modèle pour les catégories de produits"""
    name = models.CharField(max_length=200, db_index=True, verbose_name="Nom")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


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

    class Meta:
        ordering = ('-created_at',)
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

