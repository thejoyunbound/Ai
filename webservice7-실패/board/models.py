from django.db import models

# Create your models here.
class Board(models.Model):
    writer = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    cnt = models.IntegerField()

class Member(models.Model):
    user_id = models.CharField(max_length=15)
    user_pass = models.CharField(max_length=15)
    user_name = models.CharField(max_length=10)