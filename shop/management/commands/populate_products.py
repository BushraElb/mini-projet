"""
Commande Django pour peupler la base de données avec des produits High-Tech
"""
from django.core.management.base import BaseCommand
from shop.models import Category, Product


class Command(BaseCommand):
    help = 'Peuple la base de données avec des produits High-Tech'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Création des catégories...'))
        
        # Créer les catégories
        smartphones_cat, created = Category.objects.get_or_create(
            name='Smartphones',
            defaults={'description': 'Smartphones dernière génération'}
        )
        
        laptops_cat, created = Category.objects.get_or_create(
            name='Laptops',
            defaults={'description': 'Ordinateurs portables performants'}
        )
        
        accessoires_cat, created = Category.objects.get_or_create(
            name='Accessoires',
            defaults={'description': 'Accessoires High-Tech'}
        )
        
        self.stdout.write(self.style.SUCCESS('Création des produits...'))
        
        # Produits Smartphones
        smartphones = [
            {
                'name': 'iPhone 15 Pro Max 256GB',
                'category': smartphones_cat,
                'price': 1299.00,
                'stock': 15,
                'featured': True,
                'description': 'iPhone 15 Pro Max avec puce A17 Pro, écran Super Retina XDR de 6.7 pouces, triple caméra 48MP, 256GB de stockage. Design en titane premium.'
            },
            {
                'name': 'iPhone 15 128GB',
                'category': smartphones_cat,
                'price': 949.00,
                'stock': 20,
                'featured': True,
                'description': 'iPhone 15 avec puce A16 Bionic, écran Super Retina XDR de 6.1 pouces, double caméra 48MP, 128GB de stockage.'
            },
            {
                'name': 'iPhone 14 128GB',
                'category': smartphones_cat,
                'price': 799.00,
                'stock': 25,
                'description': 'iPhone 14 avec puce A15 Bionic, écran Super Retina XDR de 6.1 pouces, double caméra 12MP, 128GB de stockage.'
            },
            {
                'name': 'Samsung Galaxy S24 Ultra 256GB',
                'category': smartphones_cat,
                'price': 1249.00,
                'stock': 12,
                'featured': True,
                'description': 'Samsung Galaxy S24 Ultra avec processeur Snapdragon 8 Gen 3, écran Dynamic AMOLED 2X de 6.8 pouces, caméra 200MP, S Pen inclus, 256GB.'
            },
            {
                'name': 'Samsung Galaxy S23 256GB',
                'category': smartphones_cat,
                'price': 899.00,
                'stock': 18,
                'description': 'Samsung Galaxy S23 avec processeur Snapdragon 8 Gen 2, écran Dynamic AMOLED de 6.1 pouces, triple caméra 50MP, 256GB.'
            },
            {
                'name': 'Samsung Galaxy A54 128GB',
                'category': smartphones_cat,
                'price': 449.00,
                'stock': 30,
                'description': 'Samsung Galaxy A54 avec processeur Exynos 1380, écran Super AMOLED de 6.4 pouces, triple caméra 50MP, 128GB.'
            },
            {
                'name': 'Xiaomi Redmi Note 13 Pro 256GB',
                'category': smartphones_cat,
                'price': 349.00,
                'stock': 35,
                'description': 'Xiaomi Redmi Note 13 Pro avec processeur Snapdragon 7s Gen 2, écran AMOLED de 6.67 pouces, caméra 200MP, 256GB.'
            },
            {
                'name': 'Xiaomi Redmi 12 128GB',
                'category': smartphones_cat,
                'price': 199.00,
                'stock': 40,
                'description': 'Xiaomi Redmi 12 avec processeur MediaTek Helio G88, écran IPS LCD de 6.79 pouces, triple caméra 50MP, 128GB.'
            },
            {
                'name': 'Xiaomi Redmi Note 12 128GB',
                'category': smartphones_cat,
                'price': 249.00,
                'stock': 32,
                'description': 'Xiaomi Redmi Note 12 avec processeur Snapdragon 685, écran AMOLED de 6.67 pouces, triple caméra 48MP, 128GB.'
            },
        ]
        
        # Produits Laptops
        laptops = [
            {
                'name': 'MacBook Pro 14" M3 Pro 512GB',
                'category': laptops_cat,
                'price': 2199.00,
                'stock': 8,
                'featured': True,
                'description': 'MacBook Pro 14 pouces avec puce M3 Pro, 18 Go de mémoire unifiée, SSD 512GB, écran Liquid Retina XDR, Touch Bar.'
            },
            {
                'name': 'MacBook Air 13" M2 256GB',
                'category': laptops_cat,
                'price': 1299.00,
                'stock': 15,
                'featured': True,
                'description': 'MacBook Air 13 pouces avec puce M2, 8 Go de mémoire unifiée, SSD 256GB, écran Retina, design ultra-fin.'
            },
            {
                'name': 'MacBook Pro 16" M3 Max 1TB',
                'category': laptops_cat,
                'price': 3999.00,
                'stock': 5,
                'description': 'MacBook Pro 16 pouces avec puce M3 Max, 36 Go de mémoire unifiée, SSD 1TB, écran Liquid Retina XDR, performance maximale.'
            },
            {
                'name': 'HP Pavilion Plus 14" Intel Core i7',
                'category': laptops_cat,
                'price': 899.00,
                'stock': 12,
                'description': 'HP Pavilion Plus 14 pouces avec processeur Intel Core i7, 16 Go RAM, SSD 512GB, écran OLED 2.8K, Windows 11.'
            },
            {
                'name': 'HP Victus 15.6" AMD Ryzen 7',
                'category': laptops_cat,
                'price': 799.00,
                'stock': 10,
                'description': 'HP Victus 15.6 pouces gaming avec processeur AMD Ryzen 7, 16 Go RAM, SSD 512GB, NVIDIA RTX 4050, Windows 11.'
            },
            {
                'name': 'HP EliteBook 840 G10 Intel Core i5',
                'category': laptops_cat,
                'price': 1199.00,
                'stock': 8,
                'description': 'HP EliteBook 840 G10 professionnel avec Intel Core i5, 16 Go RAM, SSD 512GB, écran 14" FHD, Windows 11 Pro.'
            },
            {
                'name': 'Lenovo ThinkPad X1 Carbon Gen 11',
                'category': laptops_cat,
                'price': 1499.00,
                'stock': 7,
                'description': 'Lenovo ThinkPad X1 Carbon avec Intel Core i7, 16 Go RAM, SSD 512GB, écran 14" 2.8K OLED, ultra-léger et professionnel.'
            },
            {
                'name': 'Lenovo Legion 5 Pro 16" AMD Ryzen 7',
                'category': laptops_cat,
                'price': 1299.00,
                'stock': 9,
                'description': 'Lenovo Legion 5 Pro gaming 16 pouces avec AMD Ryzen 7, 16 Go RAM, SSD 1TB, NVIDIA RTX 4060, écran 165Hz.'
            },
            {
                'name': 'Lenovo Yoga 9i 14" Intel Core i7',
                'category': laptops_cat,
                'price': 1399.00,
                'stock': 6,
                'description': 'Lenovo Yoga 9i 2-en-1 avec Intel Core i7, 16 Go RAM, SSD 512GB, écran OLED 14" tactile, design convertible.'
            },
            {
                'name': 'ASUS ROG Strix G16 Intel Core i7',
                'category': laptops_cat,
                'price': 1599.00,
                'stock': 8,
                'description': 'ASUS ROG Strix G16 gaming avec Intel Core i7, 16 Go RAM, SSD 1TB, NVIDIA RTX 4070, écran 16" 165Hz.'
            },
            {
                'name': 'ASUS ZenBook 14 OLED Intel Core i5',
                'category': laptops_cat,
                'price': 999.00,
                'stock': 11,
                'description': 'ASUS ZenBook 14 OLED avec Intel Core i5, 16 Go RAM, SSD 512GB, écran OLED 14" 2.8K, design élégant et portable.'
            },
            {
                'name': 'ASUS VivoBook 15 Intel Core i5',
                'category': laptops_cat,
                'price': 599.00,
                'stock': 15,
                'description': 'ASUS VivoBook 15 avec Intel Core i5, 8 Go RAM, SSD 256GB, écran 15.6" FHD, Windows 11, excellent rapport qualité-prix.'
            },
        ]
        
        # Produits Accessoires
        accessoires = [
            {
                'name': 'AirPods Pro (2ème génération)',
                'category': accessoires_cat,
                'price': 279.00,
                'stock': 25,
                'featured': True,
                'description': 'AirPods Pro avec réduction de bruit active, audio spatial, boîtier MagSafe, autonomie jusqu\'à 30h, résistance à l\'eau IPX4.'
            },
            {
                'name': 'AirPods (3ème génération)',
                'category': accessoires_cat,
                'price': 199.00,
                'stock': 30,
                'description': 'AirPods avec audio spatial, boîtier MagSafe, autonomie jusqu\'à 30h, résistance à l\'eau IPX4, design ergonomique.'
            },
            {
                'name': 'AirPods Max',
                'category': accessoires_cat,
                'price': 599.00,
                'stock': 10,
                'description': 'AirPods Max casque over-ear avec réduction de bruit active, audio haute fidélité, autonomie 20h, design premium en aluminium.'
            },
            {
                'name': 'Sony WH-1000XM5 Casque Bluetooth',
                'category': accessoires_cat,
                'price': 399.00,
                'stock': 15,
                'featured': True,
                'description': 'Sony WH-1000XM5 avec réduction de bruit active exceptionnelle, audio haute résolution, autonomie 30h, design confortable.'
            },
            {
                'name': 'Bose QuietComfort 45',
                'category': accessoires_cat,
                'price': 329.00,
                'stock': 12,
                'description': 'Bose QuietComfort 45 avec réduction de bruit active, audio équilibré, autonomie 24h, confort exceptionnel.'
            },
            {
                'name': 'JBL Tune 770NC Casque Bluetooth',
                'category': accessoires_cat,
                'price': 99.00,
                'stock': 20,
                'description': 'JBL Tune 770NC avec réduction de bruit active, audio JBL Pure Bass, autonomie 44h, pliable et portable.'
            },
            {
                'name': 'Anker PowerCore 26800 Powerbank',
                'category': accessoires_cat,
                'price': 59.99,
                'stock': 35,
                'featured': True,
                'description': 'Anker PowerCore 26800mAh avec charge rapide Power Delivery, 3 ports USB, peut charger un iPhone jusqu\'à 6 fois.'
            },
            {
                'name': 'Xiaomi Mi Power Bank 3 20000mAh',
                'category': accessoires_cat,
                'price': 29.99,
                'stock': 40,
                'description': 'Xiaomi Mi Power Bank 3 avec capacité 20000mAh, charge rapide 18W, double port USB, design compact.'
            },
            {
                'name': 'Samsung Wireless Charger Stand',
                'category': accessoires_cat,
                'price': 49.99,
                'stock': 25,
                'description': 'Samsung Wireless Charger Stand avec charge rapide 15W, design inclinable, compatible Qi, LED indicatrice.'
            },
            {
                'name': 'Belkin BoostCharge Pro 2-en-1',
                'category': accessoires_cat,
                'price': 129.99,
                'stock': 15,
                'description': 'Belkin BoostCharge Pro chargeur 2-en-1 pour iPhone et AirPods, charge rapide MagSafe 15W, design élégant.'
            },
            {
                'name': 'Logitech MX Master 3S Souris',
                'category': accessoires_cat,
                'price': 99.99,
                'stock': 18,
                'description': 'Logitech MX Master 3S souris sans fil ergonomique, précision 8000 DPI, autonomie 70 jours, multi-appareils.'
            },
            {
                'name': 'Apple Magic Keyboard',
                'category': accessoires_cat,
                'price': 149.00,
                'stock': 12,
                'description': 'Apple Magic Keyboard avec rétroéclairage, design compact, connexion Bluetooth, compatible Mac et iPad.'
            },
        ]
        
        # Créer tous les produits
        all_products = smartphones + laptops + accessoires
        
        created_count = 0
        for product_data in all_products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'[OK] Cree: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'[EXISTE] Existe deja: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS(
            f'\nTermine! {created_count} nouveaux produits crees sur {len(all_products)} produits.'
        ))

