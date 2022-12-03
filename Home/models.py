from django.db import models

# Create your models here.

class usersinfo(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    class meta:
        db_table = "mcu"


class csv(models.Model):
    intial_velocity = models.CharField(max_length=3)
    final_velocity = models.CharField(max_length=3)
    time_taken = models.CharField(max_length=5)

    class meta:
        db_table = "mcu"