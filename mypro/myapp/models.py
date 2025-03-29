from django.db import models

from django.contrib.auth. models import User



class student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    age=models.IntegerField()