from django.db import models

# Create your models here.

class usersinfo(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    class meta:
        db_table = "mcu"


class filelog(models.Model):
    userid = models.IntegerField(null=True)
    file_name = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    algorithm = models.CharField(max_length=20,null=True)

    class meta:
        db_table = "mcu"

class candidate_algo(models.Model):
    sky = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    humid = models.CharField(max_length=50)
    wind = models.CharField(max_length=50)
    water = models.CharField(max_length=50)
    forecast = models.CharField(max_length=50)
    output = models.CharField(max_length=50)
    filename= models.CharField(max_length=100)

    class meta:
        db_table = "mcu"