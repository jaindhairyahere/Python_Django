from django.db import models

# Create your models here.
class Topic(models.Model):
	topic_name = models.CharField(max_length=200,unique=True)

	def __str__(self):
		return self.topic_name

class Website(models.Model):
	title = models.CharField(max_length=100, unique=True)
	url_address = models.URLField(unique= True)
	topic = models.ForeignKey(Topic,'')

	def __str__(self):
		return self.title

class AccessRecord(models.Model):
	name = models.ForeignKey(Website,'')
	date = models.DateField()

	def __str__(self):
		return str(self.date)

class
