from django.contrib import admin
from .models import Cart
# Register your models here.
                                                                          
class CartAdmin(admin.ModelAdmin):
    list_display=("name","quantity","price","created_at")
admin.site.register(Cart,CartAdmin) 



