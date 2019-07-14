from django.db import models
from django.contrib.auth.admin import User


# Create your models here.
class Alumni(models.Model):
	user_model = models.OneToOneField(User,'')
	name = models.CharField(max_length=100)
	phone_no = models.CharField(max_length=11,default='',blank=True)
	picture = models.ImageField(blank=True,upload_to='profile_pic')

	def __str__(self):
		return self.user_model.first_name
