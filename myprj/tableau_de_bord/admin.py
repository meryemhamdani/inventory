from django.contrib import admin
from .models import Product ,Order
admin.site.site_header = 'Tableau de bord Gestion de stock'

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)