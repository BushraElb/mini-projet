"""
Modèles pour l'application orders
"""
from django.db import models
from django.conf import settings
from shop.models import Product


class Order(models.Model):
    """Modèle pour les commandes"""
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('processing', 'En traitement'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash_on_delivery', 'Paiement à la livraison'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="Client"
    )
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=250, verbose_name="Adresse")
    postal_code = models.CharField(max_length=20, verbose_name="Code postal")
    city = models.CharField(max_length=100, verbose_name="Ville")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    paid = models.BooleanField(default=False, verbose_name="Payé")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Statut"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='cash_on_delivery',
        verbose_name="Méthode de paiement"
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'

    def __str__(self):
        return f'Commande {self.id}'

    def get_total_cost(self):
        """Calculer le coût total de la commande"""
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Modèle pour les articles d'une commande"""
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name="Commande"
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE,
        verbose_name="Produit"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantité")

    class Meta:
        verbose_name = 'Article de commande'
        verbose_name_plural = 'Articles de commande'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        """Calculer le coût de l'article"""
        return self.price * self.quantity

