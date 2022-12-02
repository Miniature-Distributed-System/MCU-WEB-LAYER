from django.db import models

# Create your models here.

class usersinfo(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)