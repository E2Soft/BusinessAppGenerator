from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=3, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=3,null=True, blank=True)
    cities = models.ManyToManyField(City, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Store(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(User)
    state = models.ForeignKey(State)
    city = models.ForeignKey(City)
    
    def __str__(self):
        return self.name
    