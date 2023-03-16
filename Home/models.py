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
    instance_type = models.CharField(max_length=20,null=True)
    aliasname = models.CharField(max_length=20,null=True,unique=True)

class devlog(models.Model):
    devid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class instances(models.Model):
    instance_name = models.CharField(max_length=20,unique=True)
    algorithm = models.CharField(max_length=20)
    csvfile = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=30)

    class meta:
        db_table = "mcu"
