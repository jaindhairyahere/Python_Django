from django.db import models
# Create your models here.
class user(models.Model):
	name = models.CharField(max_length = 100)
	product_name = models.CharField(max_length=264)
	price = models.IntegerField()