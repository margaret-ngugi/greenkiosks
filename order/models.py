from django.db import models
from customer.models import Customer
from delivery.models import Delivery
from cart.models import Cart

# Create your models here.
class Order(models.Model): 
    cart = models.ManyToManyField(Cart)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    delivery = models.OneToOneField(Delivery,null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
