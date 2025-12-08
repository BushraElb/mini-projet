"""
Context processors pour shop
"""
from .cart import Cart


def cart(request):
    """Ajouter le panier au contexte de tous les templates"""
    return {'cart': Cart(request)}

