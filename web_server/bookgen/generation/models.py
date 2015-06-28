from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    genre = models.CharField(max_length=20)

class Font(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    
class ColorPalette(models.Model):
    dark = models.CharField(max_length=6)
    med_dark = models.CharField(max_length=6)
    med_light = models.CharField(max_length=6)
    light = models.CharField(max_length=6)
    genre = models.CharField(max_length=20)