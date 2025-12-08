"""
Modèles pour l'application users
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    """Profil client étendu"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name="Utilisateur"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    address = models.CharField(max_length=250, blank=True, verbose_name="Adresse")
    postal_code = models.CharField(max_length=20, blank=True, verbose_name="Code postal")
    city = models.CharField(max_length=100, blank=True, verbose_name="Ville")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'Profil de {self.user.username}'


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    """Créer automatiquement un profil client lors de la création d'un utilisateur"""
    if created:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    """Sauvegarder le profil client lors de la sauvegarde de l'utilisateur"""
    if hasattr(instance, 'customer'):
        instance.customer.save()

