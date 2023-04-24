from django.db import models

# Create your models here.
class Armyshop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    name = models.CharField(max_length=255)
