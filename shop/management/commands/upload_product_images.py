"""
Commande Django pour uploader des images de produits depuis un dossier local
"""
from django.core.management.base import BaseCommand
from shop.models import Product
from django.core.files import File
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Upload des images de produits depuis un dossier local'

    def add_arguments(self, parser):
        parser.add_argument(
            '--folder',
            type=str,
            default='product_images',
            help='Chemin du dossier contenant les images (par défaut: product_images)'
        )
        parser.add_argument(
            '--match-by',
            type=str,
            choices=['name', 'filename', 'slug'],
            default='name',
            help='Méthode de correspondance: name (nom du produit), filename (nom du fichier), slug (slug du produit)'
        )

    def handle(self, *args, **options):
        folder_path = options['folder']
        match_by = options['match_by']
        
        # Vérifier si le dossier existe
        if not os.path.exists(folder_path):
            self.stdout.write(self.style.ERROR(
                f'Le dossier "{folder_path}" n\'existe pas. '
                f'Veuillez créer ce dossier et y placer vos images.'
            ))
            self.stdout.write(self.style.WARNING(
                f'\nExemple: Créez un dossier "product_images" à la racine du projet '
                f'et placez-y vos images avec des noms correspondant aux produits.'
            ))
            return
        
        # Obtenir tous les fichiers images du dossier
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
        image_files = []
        for ext in image_extensions:
            image_files.extend(Path(folder_path).glob(f'*{ext}'))
            image_files.extend(Path(folder_path).glob(f'*{ext.upper()}'))
        
        if not image_files:
            self.stdout.write(self.style.WARNING(
                f'Aucune image trouvée dans le dossier "{folder_path}"'
            ))
            return
        
        self.stdout.write(self.style.SUCCESS(
            f'Upload de {len(image_files)} images depuis "{folder_path}"...'
        ))
        
        updated = 0
        not_found = []
        
        for image_file in image_files:
            try:
                # Déterminer le nom de correspondance
                filename_without_ext = image_file.stem  # Nom sans extension
                
                # Trouver le produit correspondant
                product = None
                if match_by == 'name':
                    # Chercher par nom exact ou partiel
                    product = Product.objects.filter(name__icontains=filename_without_ext).first()
                elif match_by == 'filename':
                    # Le nom du fichier doit correspondre exactement au nom du produit
                    product = Product.objects.filter(name=filename_without_ext).first()
                    if not product:
                        # Essayer avec des variations (espaces, tirets, etc.)
                        product = Product.objects.filter(
                            name__iexact=filename_without_ext.replace('_', ' ').replace('-', ' ')
                        ).first()
                elif match_by == 'slug':
                    product = Product.objects.filter(slug=filename_without_ext).first()
                
                if not product:
                    not_found.append(filename_without_ext)
                    continue
                
                # Ouvrir et uploader l'image
                with open(image_file, 'rb') as f:
                    product.image.save(
                        image_file.name,
                        File(f),
                        save=True
                    )
                
                updated += 1
                self.stdout.write(self.style.SUCCESS(
                    f'[OK] Image uploadée: {product.name} <- {image_file.name}'
                ))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f'[ERREUR] {image_file.name}: {str(e)}'
                ))
                continue
        
        self.stdout.write(self.style.SUCCESS(
            f'\nTerminé! {updated} images uploadées sur {len(image_files)} fichiers.'
        ))
        
        if not_found:
            self.stdout.write(self.style.WARNING(
                f'\n{len(not_found)} images non associées (produits non trouvés):'
            ))
            for name in not_found[:10]:  # Afficher les 10 premiers
                self.stdout.write(self.style.WARNING(f'  - {name}'))
            if len(not_found) > 10:
                self.stdout.write(self.style.WARNING(f'  ... et {len(not_found) - 10} autres'))
            
            self.stdout.write(self.style.WARNING(
                f'\nConseil: Renommez vos images pour qu\'elles correspondent aux noms des produits, '
                f'ou utilisez --match-by=filename pour une correspondance exacte.'
            ))

