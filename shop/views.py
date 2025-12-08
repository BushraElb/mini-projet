"""
Vues pour l'application shop
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Category, Product
from .cart import Cart


def product_list(request, category_slug=None):
    """
    Afficher la liste des produits avec filtrage par catégorie
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    search_query = request.GET.get('search', '')

    # Filtrage par catégorie
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Recherche
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(products, 12)  # 12 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'categories': categories,
        'products': page_obj,
        'search_query': search_query,
    }
    return render(request, 'shop/shop.html', context)


def product_detail(request, id, slug):
    """
    Afficher les détails d'un produit
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/product_detail.html', context)


def cart_add(request, product_id):
    """
    Ajouter un produit au panier
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if product.stock >= quantity:
        cart.add(product=product, quantity=quantity)
        return redirect('shop:cart_detail')
    else:
        # Stock insuffisant
        return redirect('shop:product_detail', id=product.id, slug=product.slug)


def cart_remove(request, product_id):
    """
    Supprimer un produit du panier
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')


def cart_detail(request):
    """
    Afficher le panier
    """
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})


def cart_update(request, product_id):
    """
    Mettre à jour la quantité d'un produit dans le panier
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > 0 and product.stock >= quantity:
        cart.add(product=product, quantity=quantity, override_quantity=True)
    return redirect('shop:cart_detail')

