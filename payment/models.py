from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
