from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    img = models.ImageField()
    lvl = models.IntegerField()
# Create your models here.
