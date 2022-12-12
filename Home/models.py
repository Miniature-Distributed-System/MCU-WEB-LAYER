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

    class meta:
        db_table = "mcu"

