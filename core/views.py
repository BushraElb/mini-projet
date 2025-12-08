"""
Vues pour l'application core
"""
from django.shortcuts import render
from shop.models import Product


def home(request):
    """
    Page d'accueil avec produits populaires
    """
    featured_products = Product.objects.filter(featured=True, available=True)[:8]
    latest_products = Product.objects.filter(available=True).order_by('-created_at')[:8]

    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
    }
    return render(request, 'core/index.html', context)

