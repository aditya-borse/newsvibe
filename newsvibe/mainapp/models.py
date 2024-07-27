from django.db import models
 
class article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200,null=True)
    summary = models.TextField(max_length=4000)
    link = models.URLField(max_length = 2000)
    sentiment = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    thumbnail_link = models.URLField(max_length=500)
# Create your models here.
