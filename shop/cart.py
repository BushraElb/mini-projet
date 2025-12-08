"""
Gestion du panier d'achat basé sur les sessions
"""
from decimal import Decimal
from django.conf import settings


class Cart:
    """Classe pour gérer le panier dans la session"""

    def __init__(self, request):
        """
        Initialiser le panier
        """
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            # Sauvegarder un panier vide dans la session
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Ajouter un produit au panier ou mettre à jour sa quantité
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Marquer la session comme modifiée pour s'assurer qu'elle est sauvegardée"""
        self.session.modified = True

    def remove(self, product):
        """
        Supprimer un produit du panier
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Itérer sur les éléments du panier et obtenir les produits
        de la base de données
        """
        from shop.models import Product
        product_ids = self.cart.keys()
        # Obtenir les objets produits et les ajouter au panier
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Compter tous les éléments dans le panier
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculer le coût total des articles dans le panier
        """
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        """
        Vider le panier
        """
        del self.session['cart']
        self.save()

