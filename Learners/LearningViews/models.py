from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100,blank=True,null=True)
	age = models.PositiveSmallIntegerField()
	created_by = models.ForeignKey(User,on_delete=models.CASCADE)
	def print_something(self):
		return HttpResponse("This is an Student Object")
	def get_absolute_url(self):
		return reverse('student-list')

	def __str__(self):
		return self.name
