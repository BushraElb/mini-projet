"""
Vues pour l'application core
"""
from django.shortcuts import render
from shop.models import Product, Category


def home(request):
    """
    Page d'accueil avec nouveaux produits, best sellers et catégories
    """
    # Nouveaux produits (8 derniers)
    latest_products = Product.objects.filter(available=True).order_by('-created_at')[:8]
    
    # Best sellers (produits featured)
    best_sellers = Product.objects.filter(featured=True, available=True)[:8]
    
    # Catégories principales avec images
    main_categories = Category.objects.filter(is_main_category=True).exclude(name='Accessoires')
    
    # Nouveaux iPhone (utiliser display_order défini dans l'admin)
    iphone_category = Category.objects.filter(name='iPhone', parent__name='Apple').first()
    if iphone_category:
        new_iphones = Product.objects.filter(
            category=iphone_category,
            available=True
        ).order_by('display_order', 'name')[:12]
    else:
        new_iphones = Product.objects.filter(
            category__name__icontains='iPhone',
            available=True
        ).order_by('display_order', 'name')[:12]
    
    # Catégories pour les bannières (dans l'ordre spécifique)
    banner_categories = []
    category_names = ['iPhone', 'iPad', 'Macbook', 'AirPods', 'Watch', 'iMac', 'Samsung', 'Laptops', 'Gaming']
    
    for cat_name in category_names:
        if cat_name == 'Macbook':
            # Macbook peut être sous Apple ou Laptops
            cat = Category.objects.filter(name='MacBook', parent__name='Apple').first()
            if not cat:
                cat = Category.objects.filter(name='Macbook', parent__name='Laptops').first()
        elif cat_name == 'Samsung':
            # Samsung est une catégorie principale
            cat = Category.objects.filter(name='Samsung', is_main_category=True).first()
        elif cat_name == 'Laptops':
            # Laptops est une catégorie principale
            cat = Category.objects.filter(name='Laptops', is_main_category=True).first()
        elif cat_name == 'Gaming':
            # Gaming est une catégorie principale
            cat = Category.objects.filter(name='Gaming', is_main_category=True).first()
        else:
            # iPhone, iPad, AirPods, Watch, iMac sont sous Apple
            cat = Category.objects.filter(name=cat_name, parent__name='Apple').first()
        
        if cat:
            banner_categories.append(cat)

    context = {
        'latest_products': latest_products,
        'best_sellers': best_sellers,
        'categories': main_categories,
        'new_iphones': new_iphones,
        'banner_categories': banner_categories,
    }
    return render(request, 'core/index.html', context)

