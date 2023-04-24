from django.db import models

# Create your models here.

class Borad(models.Model):
    writer = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    cnt = models.IntegerField()