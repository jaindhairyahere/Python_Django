from django.db import models

# Create your models here.
class Staff(models.Model):
	name = models.CharField(max_length=128,blank=False,null=False)
	age = models.IntegerField(blank=False,null=True)
	gender_list = [
		('M','male'),
		('F','female'),
		('T','trans')
	]
	gender = models.CharField(max_length=1,choices=gender_list,default=None)
	date_of_birth = models.DateField(blank=True,null=True)
	address = models.TextField(blank=False)
	salary = models.IntegerField()

	class Meta():
		abstract = True


class Teacher(Staff):
	department = models.CharField(max_length=128)
	highest_degree = models.CharField(max_length=128)
	experience = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		print("Instance Saved!")

class Driver(Staff):
	bus_no = models.PositiveSmallIntegerField(null=True)
	area = models.CharField(max_length=512,null=True)
	experience = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		print("Instance Saved!")

class Helper(Staff):
	fields_available = [('CW','Class Worker'),('PW','Peun Worker'),
		('PA','Principal\'s Assistant'),('Te','Technecian'),('SA','School Administrator'),]
	area = models.CharField(max_length=2,choices=fields_available)
	def __str__(self):
		return self.name
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		print("Instance Saved!")

