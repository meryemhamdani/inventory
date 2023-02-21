from django.contrib import admin
from .models import Product

admin.site.site_header = 'Tableau de bord Gestion de stock'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','quantity',)
    list_filter=['category']

# Register your models here.
admin.site.register(Product ,ProductAdmin)

