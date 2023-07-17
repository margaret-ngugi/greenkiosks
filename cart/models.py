from django.db import models
from inventory.models import Product
# Create your models here.
class Cart(models.Model):
    Products=models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

