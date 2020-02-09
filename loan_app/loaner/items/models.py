from django.db import models

# Create your models here.

class Items(models.Model):
    name =  models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    value = models.DecimalField(decimal_places=2, max_digits=5)
    rate = models.DecimalField(decimal_places=2, max_digits=5)
    currentlyOut = models.BooleanField()
    owner = models.CharField(max_length=50)
    daysLeft = models.DecimalField(decimal_places=2, max_digits=5) 
    willingtoTravel = models.BooleanField()
