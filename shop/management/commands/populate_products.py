
from django.core.management.base import BaseCommand
from shop.models import Category, Product


class Command(BaseCommand):
    help = 'Peuple la base de données avec des produits High-Tech organisés par versions'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Recuperation des categories...'))
        
        # Récupérer les catégories principales
        apple_main = Category.objects.filter(name='Apple', is_main_category=True).first()
        samsung_main = Category.objects.filter(name='Samsung', is_main_category=True).first()
        laptops_main = Category.objects.filter(name='Laptops', is_main_category=True).first()
        gaming_main = Category.objects.filter(name='Gaming', is_main_category=True).first()
        
        if not apple_main or not samsung_main or not laptops_main or not gaming_main:
            self.stdout.write(self.style.ERROR('Veuillez d\'abord executer: python manage.py populate_categories'))
            return
        
        # Récupérer les sous-catégories
        iphone_cat = Category.objects.filter(name='iPhone', parent=apple_main).first()
        ipad_cat = Category.objects.filter(name='iPad', parent=apple_main).first()
        macbook_cat = Category.objects.filter(name='MacBook', parent=apple_main).first()
        imac_cat = Category.objects.filter(name='iMac', parent=apple_main).first()
        macmini_cat = Category.objects.filter(name='Mac mini', parent=apple_main).first()
        watch_cat = Category.objects.filter(name='Watch', parent=apple_main).first()
        airpods_cat = Category.objects.filter(name='AirPods', parent=apple_main).first()
        apple_accessoires_cat = Category.objects.filter(name='Accessoires', parent=apple_main).first()
        
        samsung_smartphones_cat = Category.objects.filter(name='Smartphones', parent=samsung_main).first()
        samsung_tablettes_cat = Category.objects.filter(name='Tablettes', parent=samsung_main).first()
        samsung_accessoires_cat = Category.objects.filter(name='Accessoires', parent=samsung_main).first()
        
        asus_laptop_cat = Category.objects.filter(name='Asus', parent=laptops_main).first()
        msi_laptop_cat = Category.objects.filter(name='MSI', parent=laptops_main).first()
        hp_laptop_cat = Category.objects.filter(name='HP', parent=laptops_main).first()
        dell_laptop_cat = Category.objects.filter(name='Dell', parent=laptops_main).first()
        macbook_laptop_cat = Category.objects.filter(name='Macbook', parent=laptops_main).first()
        
        msi_gaming_cat = Category.objects.filter(name='MSI', parent=gaming_main).first()
        rog_gaming_cat = Category.objects.filter(name='ROG', parent=gaming_main).first()
        hp_victus_cat = Category.objects.filter(name='HP Victus', parent=gaming_main).first()
        lenovo_legion_cat = Category.objects.filter(name='Lenovo Legion', parent=gaming_main).first()
        razer_gaming_cat = Category.objects.filter(name='Razer', parent=gaming_main).first()
        
        self.stdout.write(self.style.SUCCESS('Creation des produits...'))
        
        
        iphones = [
            
            {
                'name': 'iPhone Air 128GB',
                'category': iphone_cat,
                'price': 1099.00,
                'stock': 12,
                'featured': True,
                'description': 'iPhone Air avec puce A18 Bionic, écran Super Retina XDR, double caméra 48MP, 128GB.'
            },
            
            {
                'name': 'iPhone 17 Pro Max 256GB',
                'category': iphone_cat,
                'price': 1399.00,
                'stock': 10,
                'featured': True,
                'description': 'iPhone 17 Pro Max avec puce A18 Pro, écran Super Retina XDR de 6.9 pouces, triple caméra 48MP, 256GB. Dernière génération.'
            },
            {
                'name': 'iPhone 17 Pro 256GB',
                'category': iphone_cat,
                'price': 1199.00,
                'stock': 12,
                'featured': True,
                'description': 'iPhone 17 Pro avec puce A18 Pro, écran Super Retina XDR de 6.3 pouces, triple caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 17 128GB',
                'category': iphone_cat,
                'price': 999.00,
                'stock': 15,
                'featured': True,
                'description': 'iPhone 17 avec puce A18 Bionic, écran Super Retina XDR de 6.1 pouces, double caméra 48MP, 128GB.'
            },
            
            {
                'name': 'iPhone 16 Pro Max 256GB',
                'category': iphone_cat,
                'price': 1299.00,
                'stock': 15,
                'description': 'iPhone 16 Pro Max avec puce A18 Pro, écran Super Retina XDR de 6.7 pouces, triple caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 16 Pro 256GB',
                'category': iphone_cat,
                'price': 1099.00,
                'stock': 18,
                'description': 'iPhone 16 Pro avec puce A18 Pro, écran Super Retina XDR de 6.3 pouces, triple caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 16 128GB',
                'category': iphone_cat,
                'price': 899.00,
                'stock': 20,
                'description': 'iPhone 16 avec puce A18 Bionic, écran Super Retina XDR de 6.1 pouces, double caméra 48MP, 128GB.'
            },
            {
                'name': 'iPhone 16 Plus 256GB',
                'category': iphone_cat,
                'price': 1099.00,
                'stock': 12,
                'description': 'iPhone 16 Plus avec puce A18 Bionic, écran 6.7 pouces, double caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 16e 128GB',
                'category': iphone_cat,
                'price': 799.00,
                'stock': 18, 
                'description': 'iPhone 16e avec puce A17, écran 6.1 pouces, double caméra, 128GB.'
            },
            
            {
                'name': 'iPhone 15 Pro Max 256GB',
                'category': iphone_cat,
                'price': 1199.00,
                'stock': 12,
                'description': 'iPhone 15 Pro Max avec puce A17 Pro, écran Super Retina XDR de 6.7 pouces, triple caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 15 Pro 256GB',
                'category': iphone_cat,
                'price': 999.00,
                'stock': 15,
                'description': 'iPhone 15 Pro avec puce A17 Pro, écran Super Retina XDR de 6.1 pouces, triple caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 15 128GB',
                'category': iphone_cat,
                'price': 799.00,
                'stock': 20,
                'description': 'iPhone 15 avec puce A16 Bionic, écran Super Retina XDR de 6.1 pouces, double caméra 48MP, 128GB.'
            },
            {
                'name': 'iPhone 15 Plus 256GB',
                'category': iphone_cat,
                'price': 949.00,
                'stock': 14,
                'description': 'iPhone 15 Plus avec puce A16 Bionic, écran 6.7 pouces, double caméra 48MP, 256GB.'
            },

            {
                'name': 'iPhone 14 Pro Max 256GB',
                'category': iphone_cat,
                'price': 1099.00,
                'stock': 10,
                'description': 'iPhone 14 Pro Max avec puce A16 Bionic, écran Super Retina XDR de 6.7 pouces, triple caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 14 Pro 256GB',
                'category': iphone_cat,
                'price': 899.00,
                'stock': 12,
                'description': 'iPhone 14 Pro avec puce A16 Bionic, écran Super Retina XDR de 6.1 pouces, triple caméra 48MP, 256GB.'
            },
            {
                'name': 'iPhone 14 128GB',
                'category': iphone_cat,
                'price': 699.00,
                'stock': 18,
                'description': 'iPhone 14 avec puce A15 Bionic, écran Super Retina XDR de 6.1 pouces, double caméra 12MP, 128GB.'
            },
            {
                'name': 'iPhone 14 Plus 256GB',
                'category': iphone_cat,
                'price': 799.00,
                'stock': 12,
                'description': 'iPhone 14 Plus avec puce A15 Bionic, écran 6.7 pouces, double caméra 12MP, 256GB.'
            },
            {
                'name': 'iPhone 13 Pro Max 256GB',
                'category': iphone_cat,
                'price': 999.00,
                'stock': 8,
                'description': 'iPhone 13 Pro Max avec puce A15 Bionic, écran Super Retina XDR de 6.7 pouces, triple caméra 12MP, 256GB.'
            },
            {
                'name': 'iPhone 13 Pro 256GB',
                'category': iphone_cat,
                'price': 799.00,
                'stock': 10,
                'description': 'iPhone 13 Pro avec puce A15 Bionic, écran Super Retina XDR de 6.1 pouces, triple caméra 12MP, 256GB.'
            },
            {
                'name': 'iPhone 13 128GB',
                'category': iphone_cat,
                'price': 599.00,
                'stock': 15,
                'description': 'iPhone 13 avec puce A15 Bionic, écran Super Retina XDR de 6.1 pouces, double caméra 12MP, 128GB.'
            },
        ]
        
        ipads = [
            {
                'name': 'iPad Pro 13" M4 256GB',
                'category': ipad_cat,
                'price': 1299.00,
                'stock': 8,
                'featured': True,
                'description': 'iPad Pro 13 pouces avec puce M4, écran Liquid Retina XDR, 256GB. Dernière génération.'
            },
            {
                'name': 'iPad Pro 11" M4 256GB',
                'category': ipad_cat,
                'price': 999.00,
                'stock': 10,
                'featured': True,
                'description': 'iPad Pro 11 pouces avec puce M4, écran Liquid Retina, 256GB.'
            },
            {
                'name': 'iPad Air 13" M2 256GB',
                'category': ipad_cat,
                'price': 799.00,
                'stock': 12,
                'description': 'iPad Air 13 pouces avec puce M2, écran Liquid Retina, 256GB.'
            },
            {
                'name': 'iPad Air 11" M2 128GB',
                'category': ipad_cat,
                'price': 599.00,
                'stock': 15,
                'description': 'iPad Air 11 pouces avec puce M2, écran Liquid Retina, 128GB.'
            },
            {
                'name': 'iPad Mini 7 128GB',
                'category': ipad_cat,
                'price': 549.00,
                'stock': 18,
                'description': 'iPad Mini 7 avec puce A17, écran 8.3 pouces, 128GB.'
            },
            {
                'name': 'iPad 10.9" 64GB',
                'category': ipad_cat,
                'price': 449.00,
                'stock': 20,
                'description': 'iPad 10.9 pouces avec puce A14 Bionic, écran Retina, 64GB.'
            },
        ]
        
        
        imacs = [
            {
                'name': 'Apple iMac 24 M4 10GB GPU 10GB CPU',
                'category': imac_cat,
                'price': 2299.00,
                'stock': 6,
                'description': 'iMac 24 pouces M4 avec GPU 10 cœurs, CPU 10 cœurs, écran Retina 4.5K.'
            },
            {
                'name': 'Apple iMac 24 M4 8GB GPU 8GB CPU',
                'category': imac_cat,
                'price': 1999.00,
                'stock': 8,
                'description': 'iMac 24 pouces M4 avec GPU 8 cœurs, CPU 8 cœurs, écran Retina 4.5K.'
            },
            {
                'name': 'Apple iMac 24 M1',
                'category': imac_cat,
                'price': 1499.00,
                'stock': 10,
                'description': 'iMac 24 pouces M1, écran Retina 4.5K, design fin.'
            },
        ]
        
        
        macminis = [
            {
                'name': 'Mac Mini M4',
                'category': macmini_cat,
                'price': 999.00,
                'stock': 12,
                'description': 'Mac Mini M4, puce Apple Silicon, compact et puissant.'
            },
        ]
        
        
        macbooks = [
            {
                'name': 'MacBook Pro 16" M4 Max 1TB',
                'category': macbook_cat,
                'price': 3999.00,
                'stock': 5,
                'featured': True,
                'description': 'MacBook Pro 16" avec puce M4 Max, 36 Go RAM, SSD 1TB, écran Liquid Retina XDR. Dernière génération.'
            },
            {
                'name': 'MacBook Pro 14" M4 Pro 512GB',
                'category': macbook_cat,
                'price': 2199.00,
                'stock': 8,
                'featured': True,
                'description': 'MacBook Pro 14" avec puce M4 Pro, 18 Go RAM, SSD 512GB, écran Liquid Retina XDR.'
            },
            {
                'name': 'MacBook Air 13" M4 256GB',
                'category': macbook_cat,
                'price': 1299.00,
                'stock': 12,
                'featured': True,
                'description': 'MacBook Air 13" avec puce M4, 8 Go RAM, SSD 256GB, écran Retina.'
            },
            {
                'name': 'MacBook Pro 16" M3 Max 1TB',
                'category': macbook_cat,
                'price': 3499.00,
                'stock': 6,
                'description': 'MacBook Pro 16" avec puce M3 Max, 36 Go RAM, SSD 1TB, écran Liquid Retina XDR.'
            },
            {
                'name': 'MacBook Air 13" M3 256GB',
                'category': macbook_cat,
                'price': 1199.00,
                'stock': 10,
                'description': 'MacBook Air 13" avec puce M3, 8 Go RAM, SSD 256GB, écran Retina.'
            },
            {
                'name': 'MacBook Air 15" M3 256GB',
                'category': macbook_cat,
                'price': 1399.00,
                'stock': 9,
                'description': 'MacBook Air 15" avec puce M3, 8 Go RAM, SSD 256GB, grand écran Retina.'
            },
        ]
        
        
        watches = [
            {
                'name': 'Apple Watch Series 10 GPS 45mm',
                'category': watch_cat,
                'price': 449.00,
                'stock': 20,
                'featured': True,
                'description': 'Apple Watch Series 10 GPS 45mm, écran Always-On Retina, résistant à l\'eau.'
            },
            {
                'name': 'Apple Watch Series 9 GPS 41mm',
                'category': watch_cat,
                'price': 399.00,
                'stock': 25,
                'description': 'Apple Watch Series 9 GPS 41mm, écran Always-On Retina, résistant à l\'eau.'
            },
            {
                'name': 'Apple Watch Ultra 2 49mm',
                'category': watch_cat,
                'price': 799.00,
                'stock': 10,
                'featured': True,
                'description': 'Apple Watch Ultra 2 49mm, écran Always-On Retina, résistant à l\'eau jusqu\'à 100m.'
            },
        ]
        
        
        airpods = [
            {
                'name': 'AirPods Pro (3ème génération)',
                'category': airpods_cat,
                'price': 279.00,
                'stock': 30,
                'featured': True,
                'description': 'AirPods Pro avec réduction de bruit active, audio spatial, boîtier MagSafe, autonomie 30h.'
            },
            {
                'name': 'AirPods (3ème génération)',
                'category': airpods_cat,
                'price': 199.00,
                'stock': 35,
                'description': 'AirPods avec audio spatial, boîtier MagSafe, autonomie 30h, résistance à l\'eau IPX4.'
            },
            {
                'name': 'AirPods Max',
                'category': airpods_cat,
                'price': 599.00,
                'stock': 10,
                'featured': True,
                'description': 'AirPods Max casque over-ear avec réduction de bruit active, audio haute fidélité, autonomie 20h.'
            },
        ]
        
        
        apple_accessoires = [
            {
                'name': 'Câble USB-C vers Lightning Apple 1m',
                'category': apple_accessoires_cat,
                'price': 29.00,
                'stock': 50,
                'description': 'Câble USB-C vers Lightning Apple officiel 1 mètre, charge rapide et transfert de données.'
            },
            {
                'name': 'Câble USB-C vers USB-C Apple 2m',
                'category': apple_accessoires_cat,
                'price': 35.00,
                'stock': 45,
                'description': 'Câble USB-C vers USB-C Apple officiel 2 mètres, charge rapide jusqu\'à 100W.'
            },
            {
                'name': 'Apple AirTag (Pack de 1)',
                'category': apple_accessoires_cat,
                'price': 35.00,
                'stock': 60,
                'description': 'Apple AirTag pour localiser vos objets, réseau Find My, pile remplaçable, résistant à l\'eau.'
            },
            {
                'name': 'Adaptateur USB-C vers HDMI Apple',
                'category': apple_accessoires_cat,
                'price': 69.00,
                'stock': 25,
                'description': 'Adaptateur USB-C vers HDMI Apple, support vidéo jusqu\'à 4K, charge simultanée.'
            },
            {
                'name': 'Apple Magic Keyboard',
                'category': apple_accessoires_cat,
                'price': 129.00,
                'stock': 20,
                'description': 'Clavier Apple Magic Keyboard sans fil, rechargeable, AZERTY.'
            },
            {
                'name': 'Apple Magic Mouse',
                'category': apple_accessoires_cat,
                'price': 99.00,
                'stock': 25,
                'description': 'Apple Magic Mouse avec surface Multi-Touch, rechargeable.'
            },
            {
                'name': 'Adaptateur USB-C 20 W',
                'category': apple_accessoires_cat,
                'price': 29.00,
                'stock': 40,
                'description': 'Adaptateur USB-C 20W pour charge rapide Apple.'
            },
            {
                'name': 'Câble de Charge USB-C pour Apple Watch 1 m',
                'category': apple_accessoires_cat,
                'price': 35.00,
                'stock': 50,
                'description': 'Câble de charge USB-C pour Apple Watch, longueur 1 mètre.'
            },
        ]
        
        
        samsung_phones = [
            {
                'name': 'Samsung Galaxy S24 Ultra 256GB',
                'category': samsung_smartphones_cat,
                'price': 1249.00,
                'stock': 10,
                'featured': True,
                'description': 'Samsung Galaxy S24 Ultra avec Snapdragon 8 Gen 3, écran Dynamic AMOLED 2X 6.8", caméra 200MP, S Pen, 256GB.'
            },
            {
                'name': 'Samsung Galaxy S25 Ultra 256GB',
                'category': samsung_smartphones_cat,
                'price': 1299.00,
                'stock': 10,
                'featured': True,
                'description': 'Samsung Galaxy S25 Ultra avec Snapdragon 8 Gen 4, écran Dynamic AMOLED 2X 6.8", caméra 200MP, S Pen, 256GB.'
            },
            {
                'name': 'Samsung Galaxy S25+ 256GB',
                'category': samsung_smartphones_cat,
                'price': 1099.00,
                'stock': 12,
                'description': 'Samsung Galaxy S25+ avec Snapdragon 8 Gen 4, écran 6.7", triple caméra 50MP, 256GB.'
            },
            {
                'name': 'Samsung Galaxy S25 128GB',
                'category': samsung_smartphones_cat,
                'price': 949.00,
                'stock': 14,
                'description': 'Samsung Galaxy S25 avec Snapdragon 8 Gen 4, écran 6.2", triple caméra 50MP, 128GB.'
            },
            {
                'name': 'Samsung Galaxy S24+ 256GB',
                'category': samsung_smartphones_cat,
                'price': 999.00,
                'stock': 12,
                'description': 'Samsung Galaxy S24+ avec Snapdragon 8 Gen 3, écran Dynamic AMOLED 6.7", triple caméra 50MP, 256GB.'
            },
            {
                'name': 'Samsung Galaxy S24 128GB',
                'category': samsung_smartphones_cat,
                'price': 799.00,
                'stock': 15,
                'description': 'Samsung Galaxy S24 avec Snapdragon 8 Gen 3, écran Dynamic AMOLED 6.2", triple caméra 50MP, 128GB.'
            },
            {
                'name': 'Samsung Galaxy Z Fold 7',
                'category': samsung_smartphones_cat,
                'price': 1999.00,
                'stock': 6,
                'description': 'Galaxy Z Fold 7 pliable, grand écran AMOLED, Snapdragon dernière génération.'
            },
            {
                'name': 'Samsung Galaxy Flip 7',
                'category': samsung_smartphones_cat,
                'price': 1399.00,
                'stock': 8,
                'description': 'Galaxy Flip 7 compact, écran AMOLED pliable, Snapdragon dernière génération.'
            },
            {
                'name': 'Samsung Galaxy Z Fold 6',
                'category': samsung_smartphones_cat,
                'price': 1899.00,
                'stock': 8,
                'description': 'Galaxy Z Fold 6 pliable, Snapdragon 8 Gen 3, écran pliable.'
            },
            {
                'name': 'Samsung Galaxy Flip 6',
                'category': samsung_smartphones_cat,
                'price': 1299.00,
                'stock': 10,
                'description': 'Galaxy Flip 6 compact, Snapdragon 8 Gen 3, écran pliable.'
            },
            {
                'name': 'Samsung Galaxy S23 Ultra 256GB',
                'category': samsung_smartphones_cat,
                'price': 1099.00,
                'stock': 8,
                'description': 'Samsung Galaxy S23 Ultra avec Snapdragon 8 Gen 2, écran Dynamic AMOLED 2X 6.8", caméra 200MP, 256GB.'
            },
            {
                'name': 'Samsung Galaxy S23 256GB',
                'category': samsung_smartphones_cat,
                'price': 849.00,
                'stock': 10,
                'description': 'Samsung Galaxy S23 avec Snapdragon 8 Gen 2, écran Dynamic AMOLED 6.1", triple caméra 50MP, 256GB.'
            },
        ]
        
        
        samsung_tablettes = [
            {
                'name': 'Samsung Galaxy Tab S9 Ultra 256GB',
                'category': samsung_tablettes_cat,
                'price': 1099.00,
                'stock': 8,
                'featured': True,
                'description': 'Samsung Galaxy Tab S9 Ultra 14.6", processeur Snapdragon 8 Gen 2, 256GB, S Pen inclus.'
            },
            {
                'name': 'Samsung Galaxy Tab S9+ 256GB',
                'category': samsung_tablettes_cat,
                'price': 899.00,
                'stock': 10,
                'description': 'Samsung Galaxy Tab S9+ 12.4", processeur Snapdragon 8 Gen 2, 256GB, S Pen inclus.'
            },
            {
                'name': 'Samsung Galaxy Tab S9 FE',
                'category': samsung_tablettes_cat,
                'price': 599.00,
                'stock': 12,
                'description': 'Galaxy Tab S9 FE avec écran 10.9", S Pen inclus, excellent rapport qualité/prix.'
            },
            {
                'name': 'Galaxy Tab A9',
                'category': samsung_tablettes_cat,
                'price': 249.00,
                'stock': 20,
                'description': 'Galaxy Tab A9 tablette abordable 8.7 pouces, idéale multimédia.'
            },
            {
                'name': 'Galaxy Tab A9+',
                'category': samsung_tablettes_cat,
                'price': 299.00,
                'stock': 18,
                'description': 'Galaxy Tab A9+ avec écran 11 pouces, bon rapport qualité/prix.'
            },
            {
                'name': 'Galaxy Tab A8',
                'category': samsung_tablettes_cat,
                'price': 229.00,
                'stock': 22,
                'description': 'Galaxy Tab A8, écran 10.5 pouces, idéale pour la famille.'
            },
        ]
        
        
        samsung_accessoires = [
            {
                'name': 'Samsung Galaxy Watch 7 44mm',
                'category': samsung_accessoires_cat,
                'price': 349.00,
                'stock': 15,
                'description': 'Samsung Galaxy Watch 7 44mm, écran AMOLED, résistant à l\'eau, suivi santé avancé.'
            },
            {
                'name': 'Samsung Galaxy Watch 6 Classic 47mm',
                'category': samsung_accessoires_cat,
                'price': 399.00,
                'stock': 12,
                'description': 'Samsung Galaxy Watch 6 Classic 47mm, écran AMOLED, bezel rotatif, résistant à l\'eau.'
            },
            {
                'name': 'Samsung Galaxy Buds3 Pro',
                'category': samsung_accessoires_cat,
                'price': 229.00,
                'stock': 20,
                'description': 'Samsung Galaxy Buds3 Pro avec réduction de bruit active, audio haute qualité, autonomie 30h.'
            },
        ]
        
        
        asus_laptops = [
            {
                'name': 'ASUS ZenBook 14 OLED Intel Core i5',
                'category': asus_laptop_cat,
                'price': 999.00,
                'stock': 11,
                'description': 'ASUS ZenBook 14 OLED Intel Core i5, 16 Go RAM, SSD 512GB, écran OLED 14" 2.8K.'
            },
            {
                'name': 'ASUS VivoBook 15 Intel Core i5',
                'category': asus_laptop_cat,
                'price': 599.00,
                'stock': 15,
                'description': 'ASUS VivoBook 15 Intel Core i5, 8 Go RAM, SSD 256GB, écran 15.6" FHD, Windows 11.'
            },
        ]
        
        
        msi_laptops = [
            {
                'name': 'MSI Modern 14 Intel Core i7',
                'category': msi_laptop_cat,
                'price': 899.00,
                'stock': 8,
                'description': 'MSI Modern 14 Intel Core i7, 16 Go RAM, SSD 512GB, écran 14" FHD, Windows 11.'
            },
        ]
        
        
        hp_laptops = [
            {
                'name': 'HP Pavilion Plus 14" Intel Core i7',
                'category': hp_laptop_cat,
                'price': 899.00,
                'stock': 12,
                'description': 'HP Pavilion Plus 14" Intel Core i7, 16 Go RAM, SSD 512GB, écran OLED 2.8K, Windows 11.'
            },
            {
                'name': 'HP EliteBook 840 G10 Intel Core i5',
                'category': hp_laptop_cat,
                'price': 1199.00,
                'stock': 8,
                'description': 'HP EliteBook 840 G10 professionnel, Intel Core i5, 16 Go RAM, SSD 512GB, écran 14" FHD.'
            },
        ]
        
        
        dell_laptops = [
            {
                'name': 'Dell XPS 13 Intel Core i7',
                'category': dell_laptop_cat,
                'price': 1299.00,
                'stock': 7,
                'description': 'Dell XPS 13 Intel Core i7, 16 Go RAM, SSD 512GB, écran 13.4" FHD+, Windows 11.'
            },
            {
                'name': 'Dell Inspiron 15 Intel Core i5',
                'category': dell_laptop_cat,
                'price': 699.00,
                'stock': 10,
                'description': 'Dell Inspiron 15 Intel Core i5, 8 Go RAM, SSD 256GB, écran 15.6" FHD, Windows 11.'
            },
        ]
        
        
        macbook_laptops = [
            {
                'name': 'MacBook Pro 16" M4 Max 1TB',
                'category': macbook_laptop_cat,
                'price': 3999.00,
                'stock': 5,
                'featured': True,
                'description': 'MacBook Pro 16" avec puce M4 Max, 36 Go RAM, SSD 1TB, écran Liquid Retina XDR.'
            },
            {
                'name': 'MacBook Air 13" M4 256GB',
                'category': macbook_laptop_cat,
                'price': 1299.00,
                'stock': 12,
                'featured': True,
                'description': 'MacBook Air 13" avec puce M4, 8 Go RAM, SSD 256GB, écran Retina.'
            },
        ]
        
        
        msi_gaming = [
            {
                'name': 'MSI Raider GE78 HX 17" Intel i9 RTX 4090',
                'category': msi_gaming_cat,
                'price': 3499.00,
                'stock': 3,
                'featured': True,
                'description': 'MSI Raider GE78 HX 17" Intel Core i9, RTX 4090, 32 Go RAM, SSD 2TB, écran 17" 240Hz.'
            },
            {
                'name': 'MSI Stealth 16" Intel i7 RTX 4070',
                'category': msi_gaming_cat,
                'price': 1999.00,
                'stock': 5,
                'description': 'MSI Stealth 16" Intel Core i7, RTX 4070, 16 Go RAM, SSD 1TB, écran 16" 165Hz.'
            },
        ]
        
        
        rog_gaming = [
            {
                'name': 'ASUS ROG Strix G18 Intel i9 RTX 4080',
                'category': rog_gaming_cat,
                'price': 2999.00,
                'stock': 4,
                'featured': True,
                'description': 'ASUS ROG Strix G18 Intel Core i9, RTX 4080, 32 Go RAM, SSD 2TB, écran 18" 165Hz.'
            },
            {
                'name': 'ASUS ROG Zephyrus G16 Intel i7 RTX 4070',
                'category': rog_gaming_cat,
                'price': 2199.00,
                'stock': 6,
                'description': 'ASUS ROG Zephyrus G16 Intel Core i7, RTX 4070, 16 Go RAM, SSD 1TB, écran 16" 165Hz.'
            },
        ]
        
        
        hp_victus = [
            {
                'name': 'HP Victus 16" AMD Ryzen 7 RTX 4060',
                'category': hp_victus_cat,
                'price': 1299.00,
                'stock': 8,
                'description': 'HP Victus 16" AMD Ryzen 7, RTX 4060, 16 Go RAM, SSD 512GB, écran 16" 144Hz.'
            },
            {
                'name': 'HP Victus 15.6" AMD Ryzen 7 RTX 4050',
                'category': hp_victus_cat,
                'price': 999.00,
                'stock': 10,
                'description': 'HP Victus 15.6" AMD Ryzen 7, RTX 4050, 16 Go RAM, SSD 512GB, écran 15.6" 144Hz.'
            },
        ]
        
        
        lenovo_legion = [
            {
                'name': 'Lenovo Legion Pro 7i 16" Intel i9 RTX 4090',
                'category': lenovo_legion_cat,
                'price': 3299.00,
                'stock': 3,
                'featured': True,
                'description': 'Lenovo Legion Pro 7i 16" Intel Core i9, RTX 4090, 32 Go RAM, SSD 2TB, écran 16" 240Hz.'
            },
            {
                'name': 'Lenovo Legion 5 Pro 16" AMD Ryzen 7 RTX 4060',
                'category': lenovo_legion_cat,
                'price': 1299.00,
                'stock': 9,
                'description': 'Lenovo Legion 5 Pro 16" AMD Ryzen 7, RTX 4060, 16 Go RAM, SSD 1TB, écran 16" 165Hz.'
            },
        ]
        
        
        razer_gaming = [
            {
                'name': 'Razer Blade 18 Intel i9 RTX 4090',
                'category': razer_gaming_cat,
                'price': 4499.00,
                'stock': 2,
                'featured': True,
                'description': 'Razer Blade 18 Intel Core i9, RTX 4090, 32 Go RAM, SSD 2TB, écran 18" 240Hz QHD+.'
            },
            {
                'name': 'Razer Blade 16 Intel i9 RTX 4080',
                'category': razer_gaming_cat,
                'price': 3499.00,
                'stock': 4,
                'description': 'Razer Blade 16 Intel Core i9, RTX 4080, 32 Go RAM, SSD 1TB, écran 16" 240Hz QHD+.'
            },
        ]
        
        
        all_products = (
            iphones + ipads + imacs + macminis + macbooks + watches + airpods + apple_accessoires +
            samsung_phones + samsung_tablettes + samsung_accessoires +
            asus_laptops + msi_laptops + hp_laptops + dell_laptops + macbook_laptops +
            msi_gaming + rog_gaming + hp_victus + lenovo_legion + razer_gaming
        )
        
        created_count = 0
        updated_count = 0
        for product_data in all_products:
            if product_data['category']:  # Vérifier que la catégorie existe
                product, created = Product.objects.get_or_create(
                    name=product_data['name'],
                    defaults=product_data
                )
                if created:
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f'[OK] Cree: {product.name}'))
                else:
                    
                    if 'display_order' in product_data:
                        product.display_order = product_data['display_order']
                        product.save()
                        updated_count += 1
                    self.stdout.write(self.style.WARNING(f'[EXISTE] Existe deja: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS(
            f'\nTermine! {created_count} nouveaux produits crees, {updated_count} produits mis a jour sur {len(all_products)} produits.'
        ))


