"""
Configuration admin pour shop
"""
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'is_main_category', 'order', 'image', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['is_main_category', 'parent', 'created_at']
    list_editable = ['is_main_category', 'order']
    fields = ['name', 'slug', 'description', 'image', 'parent', 'is_main_category', 'order']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'featured', 'display_order', 'created_at']
    list_filter = ['available', 'created_at', 'updated_at', 'category', 'featured']
    list_editable = ['price', 'stock', 'available', 'featured', 'display_order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    raw_id_fields = ['category']

