from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group
admin.site.site_header = 'Tableau de bord Gestion de stock'
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ['category']
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)