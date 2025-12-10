"""
Commande Django pour ajouter des images placeholder aux produits
"""
from django.core.management.base import BaseCommand
from shop.models import Product
import requests
from io import BytesIO
from django.core.files.base import ContentFile
import random


class Command(BaseCommand):
    help = 'Ajoute des images placeholder aux produits sans image'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Ajout des images aux produits...'))
        
        # Mapping des catégories vers des URLs d'images spécifiques
        category_image_map = {
            'iPhone': [
                'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=800&fit=crop',
            ],
            'iPad': [
                'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1561154464-82e9adf32764?w=800&h=800&fit=crop',
            ],
            'MacBook': [
                'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800&h=800&fit=crop',
            ],
            'Watch': [
                'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=800&h=800&fit=crop',
            ],
            'AirPods': [
                'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=800&h=800&fit=crop',
            ],
            'Smartphones': [
                'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800&h=800&fit=crop',
            ],
            'Tablettes': [
                'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&h=800&fit=crop',
            ],
            'default': [
                'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=800&fit=crop',
            ]
        }
        
        # Produits sans images
        products = Product.objects.filter(image='') | Product.objects.filter(image__isnull=True)
        total = products.count()
        updated = 0
        
        if total == 0:
            self.stdout.write(self.style.WARNING('Tous les produits ont deja une image.'))
            return
        
        for product in products:
            try:
                # Déterminer quelle catégorie d'images utiliser
                category_name = product.category.name
                image_urls = category_image_map.get(category_name, category_image_map['default'])
                
                # Sélectionner une URL d'image aléatoire
                image_url = random.choice(image_urls)
                
                # Télécharger l'image
                response = requests.get(image_url, timeout=15)
                response.raise_for_status()
                
                # Créer un nom de fichier basé sur le nom du produit
                filename = f"{product.slug or product.name.replace(' ', '_').lower()}.jpg"
                
                # Sauvegarder l'image
                product.image.save(
                    filename,
                    ContentFile(response.content),
                    save=True
                )
                
                updated += 1
                self.stdout.write(self.style.SUCCESS(f'[OK] Image ajoutee: {product.name}'))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'[ERREUR] {product.name}: {str(e)}'))
                continue
        
        self.stdout.write(self.style.SUCCESS(
            f'\nTermine! {updated} images ajoutees sur {total} produits.'
        ))
