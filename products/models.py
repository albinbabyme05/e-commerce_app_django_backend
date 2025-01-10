from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE =1
    DELETE =0
    DELETE_CHOICES = ((LIVE,'live'),(DELETE,'Delete'))
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    priority =models.IntegerField(default=0)
    deleteStatus = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title