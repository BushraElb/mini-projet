"""
Context processors pour shop
"""
from .cart import Cart
from .models import Category


def cart(request):
    """Ajouter le panier au contexte de tous les templates"""
    return {'cart': Cart(request)}


def main_categories(request):
    """Ajouter les catégories principales au contexte"""
    main_cats = Category.objects.filter(is_main_category=True).prefetch_related('children')
    return {'main_categories': main_cats}

