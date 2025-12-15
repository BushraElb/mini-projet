"""
Vues pour l'application orders
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderCreateForm
from shop.cart import Cart
from users.models import Customer


@login_required
def order_create(request):
    """
    Créer une nouvelle commande
    """
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'Votre panier est vide.')
        return redirect('shop:product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.paid = False  # Paiement à la livraison
            order.save()

            # Créer les articles de commande
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                # Réduire le stock
                product = item['product']
                product.stock -= item['quantity']
                product.save()

            # Vider le panier
            cart.clear()
            messages.success(request, f'Votre commande #{order.id} a été créée avec succès!')
            return redirect('orders:order_success', order_id=order.id)
    else:
        # Pré-remplir le formulaire avec les données de l'utilisateur
        if request.user.is_authenticated:
            # Créer le profil Customer s'il n'existe pas
            customer, created = Customer.objects.get_or_create(user=request.user)
            initial_data = {
                'first_name': request.user.first_name or '',
                'last_name': request.user.last_name or '',
                'email': request.user.email or '',
                'address': customer.address or '',
                'postal_code': customer.postal_code or '',
                'city': customer.city or '',
                'phone': customer.phone or '',
            }
        else:
            initial_data = {}
        form = OrderCreateForm(initial=initial_data)

    return render(request, 'orders/checkout.html', {
        'cart': cart,
        'form': form,
    })


@login_required
def order_success(request, order_id):
    """
    Page de confirmation de commande
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})


@login_required
def order_list(request):
    """
    Liste des commandes de l'utilisateur
    """
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """
    Détails d'une commande
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def order_invoice(request, order_id):
    """
    Facture imprimable d'une commande
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/invoice.html', {'order': order})

