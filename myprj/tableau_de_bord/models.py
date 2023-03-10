from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY = (
    ('bureau', 'bureau'),
    ('Electronics', 'Electronics'),
    ('portable', 'portable'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'
    def _str_(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Order'

    def str(self):
        return f'{self.name} commander par {self.customer}'