# Create your models here.
from django.db import models


class category(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pic")
    
    
class films(models.Model):
    pro=models.ForeignKey(category,related_name="category",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pic")
    rating=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    screen=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    seatsavai=models.IntegerField(default=0)  
    price = models.DecimalField(decimal_places=2, max_digits=6)
    time = models.TimeField()