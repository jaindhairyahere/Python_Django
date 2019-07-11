from django.db import models
from datetime import date
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length =264)
    dob = models.DateField(default= date.today())
    email = models.CharField(unique=True, max_length=100)

class Company(models.Model):
    com_id = models.ForeignKey(Person,'')
    name = models.CharField(max_length=264)
