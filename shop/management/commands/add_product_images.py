"""
Commande Django pour ajouter des images placeholder aux produits
"""
from django.core.management.base import BaseCommand
from shop.models import Product
import requests
from io import BytesIO
from django.core.files import File
import random


class Command(BaseCommand):
    help = 'Ajoute des images placeholder aux produits sans image'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Ajout des images aux produits...'))
        
        # Liste d'URLs d'images placeholder (Unsplash)
        # Images High-Tech / Tech products
        image_urls = [
            'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=800&fit=crop',  # Smartphone
            'https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=800&h=800&fit=crop',  # iPhone
            'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800&h=800&fit=crop',  # Smartphone
            'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=800&fit=crop',  # Laptop
            'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=800&fit=crop',  # MacBook
            'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800&h=800&fit=crop',  # Laptop
            'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=800&fit=crop',  # Headphones
            'https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=800&h=800&fit=crop',  # AirPods
            'https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=800&h=800&fit=crop',  # Powerbank
            'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800&h=800&fit=crop',  # Tech accessories
        ]
        
        products = Product.objects.filter(image='')
        total = products.count()
        updated = 0
        
        if total == 0:
            self.stdout.write(self.style.WARNING('Tous les produits ont deja une image.'))
            return
        
        for product in products:
            try:
                # Sélectionner une URL d'image aléatoire
                image_url = random.choice(image_urls)
                
                # Télécharger l'image
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()
                
                # Créer un nom de fichier basé sur le nom du produit
                filename = f"{product.slug or product.name.replace(' ', '_').lower()}.jpg"
                
                # Sauvegarder l'image
                image_file = BytesIO(response.content)
                product.image.save(filename, File(image_file), save=True)
                
                updated += 1
                self.stdout.write(self.style.SUCCESS(f'[OK] Image ajoutee: {product.name}'))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'[ERREUR] {product.name}: {str(e)}'))
                continue
        
        self.stdout.write(self.style.SUCCESS(
            f'\nTermine! {updated} images ajoutees sur {total} produits.'
        ))

