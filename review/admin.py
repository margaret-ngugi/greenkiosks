from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display=("author","content","rating","date_posted")
admin.site.register(Review,ReviewAdmin) 
