"""
Commande Django pour créer les catégories principales et sous-catégories
"""
from django.core.management.base import BaseCommand
from shop.models import Category


class Command(BaseCommand):
    help = 'Crée les catégories principales et sous-catégories'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creation des categories...'))
        
        # NE PAS supprimer les catégories existantes pour préserver les produits
        
        # ========== APPLE ==========
        apple_main, created = Category.objects.get_or_create(
            name='Apple',
            defaults={
                'is_main_category': True,
                'description': 'Produits Apple',
                'slug': 'apple',
                'order': 1
            }
        )
        if not created:
            apple_main.order = 1
            apple_main.save()
        
        apple_subcategories = [
            {'name': 'iPhone', 'description': 'Smartphones iPhone', 'slug': 'apple-iphone', 'order': 1},
            {'name': 'iPad', 'description': 'Tablettes iPad', 'slug': 'apple-ipad', 'order': 2},
            {'name': 'MacBook', 'description': 'Ordinateurs portables MacBook', 'slug': 'apple-macbook', 'order': 3},
            {'name': 'iMac', 'description': 'Ordinateurs de bureau iMac', 'slug': 'apple-imac', 'order': 4},
            {'name': 'Mac mini', 'description': 'Mac mini', 'slug': 'apple-mac-mini', 'order': 5},
            {'name': 'Watch', 'description': 'Apple Watch', 'slug': 'apple-watch', 'order': 6},
            {'name': 'AirPods', 'description': 'Écouteurs AirPods', 'slug': 'apple-airpods', 'order': 7},
            {'name': 'Accessoires', 'description': 'Accessoires Apple', 'slug': 'apple-accessoires', 'order': 8},
        ]
        
        for subcat_data in apple_subcategories:
            cat, created = Category.objects.get_or_create(
                name=subcat_data['name'],
                parent=apple_main,
                defaults={
                    'description': subcat_data['description'],
                    'order': subcat_data['order']
                }
            )
            if not created:
                cat.order = subcat_data['order']
                if not cat.slug:
                    cat.slug = subcat_data['slug']
                cat.save()
        
        # ========== SAMSUNG ==========
        samsung_main, created = Category.objects.get_or_create(
            name='Samsung',
            defaults={
                'is_main_category': True,
                'description': 'Produits Samsung',
                'slug': 'samsung',
                'order': 2
            }
        )
        if not created:
            samsung_main.order = 2
            samsung_main.save()
        
        samsung_subcategories = [
            {'name': 'Smartphones', 'description': 'Smartphones Samsung', 'slug': 'samsung-smartphones', 'order': 1},
            {'name': 'Tablettes', 'description': 'Tablettes Samsung', 'slug': 'samsung-tablettes', 'order': 2},
            {'name': 'Accessoires', 'description': 'Accessoires Samsung', 'slug': 'samsung-accessoires', 'order': 3},
        ]
        
        for subcat_data in samsung_subcategories:
            cat, created = Category.objects.get_or_create(
                name=subcat_data['name'],
                parent=samsung_main,
                defaults={
                    'description': subcat_data['description'],
                    'order': subcat_data['order']
                }
            )
            if not created:
                cat.order = subcat_data['order']
                if not cat.slug:
                    cat.slug = subcat_data['slug']
                cat.save()
        
        # ========== LAPTOPS ==========
        laptops_main, created = Category.objects.get_or_create(
            name='Laptops',
            defaults={
                'is_main_category': True,
                'description': 'Ordinateurs portables',
                'slug': 'laptops',
                'order': 3
            }
        )
        if not created:
            laptops_main.order = 3
            laptops_main.save()
        
        # Récupérer MacBook d'Apple pour le réutiliser
        apple_macbook = Category.objects.filter(name='MacBook', parent=apple_main).first()
        
        laptops_subcategories = [
            {'name': 'Asus', 'description': 'Laptops Asus', 'slug': 'laptops-asus', 'order': 1},
            {'name': 'MSI', 'description': 'Laptops MSI', 'slug': 'laptops-msi', 'order': 2},
            {'name': 'HP', 'description': 'Laptops HP', 'slug': 'laptops-hp', 'order': 3},
            {'name': 'Dell', 'description': 'Laptops Dell', 'slug': 'laptops-dell', 'order': 4},
        ]
        
        for subcat_data in laptops_subcategories:
            cat, created = Category.objects.get_or_create(
                name=subcat_data['name'],
                parent=laptops_main,
                defaults={
                    'description': subcat_data['description'],
                    'order': subcat_data['order']
                }
            )
            if not created:
                cat.order = subcat_data['order']
                if not cat.slug:
                    cat.slug = subcat_data['slug']
                cat.save()
        
        # ========== GAMING ==========
        gaming_main, created = Category.objects.get_or_create(
            name='Gaming',
            defaults={
                'is_main_category': True,
                'description': 'Laptops Gaming',
                'slug': 'gaming',
                'order': 4
            }
        )
        if not created:
            gaming_main.order = 4
            gaming_main.save()
        
        gaming_subcategories = [
            {'name': 'MSI', 'description': 'Laptops Gaming MSI', 'slug': 'gaming-msi', 'order': 1},
            {'name': 'ROG', 'description': 'Laptops Gaming ASUS ROG', 'slug': 'gaming-rog', 'order': 2},
            {'name': 'HP Victus', 'description': 'Laptops Gaming HP Victus', 'slug': 'gaming-hp-victus', 'order': 3},
            {'name': 'Lenovo Legion', 'description': 'Laptops Gaming Lenovo Legion', 'slug': 'gaming-lenovo-legion', 'order': 4},
            {'name': 'Razer', 'description': 'Laptops Gaming Razer', 'slug': 'gaming-razer', 'order': 5},
        ]
        
        for subcat_data in gaming_subcategories:
            cat, created = Category.objects.get_or_create(
                name=subcat_data['name'],
                parent=gaming_main,
                defaults={
                    'description': subcat_data['description'],
                    'order': subcat_data['order']
                }
            )
            if not created:
                cat.order = subcat_data['order']
                if not cat.slug:
                    cat.slug = subcat_data['slug']
                cat.save()
        
        # ========== ACCESSOIRES (catégorie principale) ==========
        # Vérifier si une catégorie Accessoires principale existe déjà
        accessoires_main = Category.objects.filter(name='Accessoires', is_main_category=True).first()
        if not accessoires_main:
            accessoires_main = Category.objects.create(
                name='Accessoires',
                is_main_category=True,
                description='Accessoires High-Tech',
                slug='accessoires'
            )
        
        self.stdout.write(self.style.SUCCESS('\nTermine! Categories principales et sous-categories creees.'))
