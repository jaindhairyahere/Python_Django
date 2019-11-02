from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField(max_length=50)
    rating = models.TextField(max_length=100)
    release_date = models.TextField(max_length=100)
    duration = models.TextField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title
    