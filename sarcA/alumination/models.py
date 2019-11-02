from django.db import models
from django.core import validators

# Create your models here.
class Person(models.Model):
	name = models.TextField(max_length=50)
	age = models.TextField()
	email = models.EmailField()
	phone_no = models.TextField(max_length=10)
	class Meta:
		abstract = True

class Workshops(Person):
	''' Workshop '''
	work = models.TextField(max_length=100)
	class Meta:
		pass

class SpeedMentoring(Person):
	''' Speed Mentoring '''
	review = models.TextField(max_length=200)
	class Meta:
		pass

class MIGD(Person):
	''' MIGD '''
	query = models.TextField(max_length=200)
	class Meta:
		pass
