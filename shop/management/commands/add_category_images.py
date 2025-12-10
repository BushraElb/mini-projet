"""
Commande Django pour ajouter des images placeholder aux catégories
"""
from django.core.management.base import BaseCommand
from shop.models import Category
from django.db import models
import requests
from io import BytesIO
from django.core.files.base import ContentFile
import random


class Command(BaseCommand):
    help = 'Ajoute des images placeholder aux catégories sans image'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Ajout des images aux categories...'))
        
        # Mapping des catégories vers des URLs d'images spécifiques
        category_image_map = {
            'Apple': [
                'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=800&fit=crop',
            ],
            'Samsung': [
                'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800&h=800&fit=crop',
            ],
            'Laptops': [
                'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=800&fit=crop',
            ],
            'Gaming': [
                'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=800&fit=crop',
            ],
            'iPhone': [
                'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=800&fit=crop',
                'https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=800&h=800&fit=crop',
            ],
            'iPad': [
                'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&h=800&fit=crop',
            ],
            'MacBook': [
                'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=800&fit=crop',
            ],
            'Watch': [
                'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=800&fit=crop',
            ],
            'AirPods': [
                'https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=800&h=800&fit=crop',
            ],
            'default': [
                'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=800&fit=crop',
            ]
        }
        
        # Catégories sans images (principales uniquement)
        categories = Category.objects.filter(
            is_main_category=True
        ).filter(
            models.Q(image='') | models.Q(image__isnull=True)
        )
        total = categories.count()
        updated = 0
        
        if total == 0:
            self.stdout.write(self.style.WARNING('Toutes les categories principales ont deja une image.'))
            return
        
        for category in categories:
            try:
                # Déterminer quelle catégorie d'images utiliser
                category_name = category.name
                image_urls = category_image_map.get(category_name, category_image_map['default'])
                
                # Sélectionner une URL d'image aléatoire
                image_url = random.choice(image_urls)
                
                # Télécharger l'image
                response = requests.get(image_url, timeout=15)
                response.raise_for_status()
                
                # Créer un nom de fichier basé sur le nom de la catégorie
                filename = f"{category.slug or category.name.replace(' ', '_').lower()}.jpg"
                
                # Sauvegarder l'image
                category.image.save(
                    filename,
                    ContentFile(response.content),
                    save=True
                )
                
                updated += 1
                self.stdout.write(self.style.SUCCESS(f'[OK] Image ajoutee: {category.name}'))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'[ERREUR] {category.name}: {str(e)}'))
                continue
        
        self.stdout.write(self.style.SUCCESS(
            f'\nTermine! {updated} images ajoutees sur {total} categories.'
        ))

