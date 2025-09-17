from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/', default='movie/images/default.JPG')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Signup(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email