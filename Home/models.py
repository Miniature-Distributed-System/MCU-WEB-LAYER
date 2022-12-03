from django.db import models

# Create your models here.

class usersinfo(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    class meta:
        db_table = "mcu"


class csv(models.Model):
    Intvelocity = models.CharField(max_length=3)
    finvelocity = models.CharField(max_length=3)
    ETime = models.CharField(max_length=5)

    class meta:
        db_table = "mcu"