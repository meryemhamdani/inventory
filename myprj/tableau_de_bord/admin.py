from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group

admin.site.site_header = "Gestion de stock dashboard"
admin.site.site_header = 'Tableau de bord Gestion de stock'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category',]

# Register your models here.
admin.site.register(Product, ProductAdmin)
#admin.site.unregister(Group)
