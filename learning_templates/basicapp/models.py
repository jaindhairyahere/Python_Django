from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
	name = models.CharField(max_length = 100)
	product_name = models.CharField(max_length=264)
	price = models.IntegerField()

class UserProfileInfo(models.Model):

	password = models.OneToOneField(User,on_delete='')

	portfolio = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return self.user.username


