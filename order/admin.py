from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=("quantity","customer_name","order_date")
admin.site.register(Order,OrderAdmin) 
