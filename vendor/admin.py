from django.contrib import admin
from .models import Vendor

# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display=("firstName","lastName","email","userName","password","date_updated")
admin.site.register(Vendor,VendorAdmin) 

