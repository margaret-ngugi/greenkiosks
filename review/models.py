from django.db import models
# Create your models here.
class Review(models.Model):
    author = models.CharField(max_length=100)  
    content = models.TextField()  
    rating = models.IntegerField()  
    date_posted = models.DateTimeField(auto_now_add=True)
