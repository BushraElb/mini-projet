"""
Vues pour l'application users
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, CustomerUpdateForm
from .models import Customer


def register(request):
    """
    Inscription d'un nouvel utilisateur
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username}!')
            login(request, user)
            return redirect('core:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    Profil utilisateur avec possibilité de mise à jour
    """
    # Créer le profil Customer s'il n'existe pas
    customer, created = Customer.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        customer_form = CustomerUpdateForm(
            request.POST,
            instance=customer
        )
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(request, 'Votre profil a été mis à jour!')
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        customer_form = CustomerUpdateForm(instance=customer)

    context = {
        'user_form': user_form,
        'customer_form': customer_form,
    }
    return render(request, 'users/profile.html', context)

