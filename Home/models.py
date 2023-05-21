from django.db import models

# Create your models here.

class usersinfo(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class filelog(models.Model):
    userid = models.IntegerField(null=True)
    file_name = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    instance_type = models.CharField(max_length=20,null=True)
    aliasname = models.CharField(max_length=50,unique=True,primary_key=True,default='SOME STRING')
    timestamp = models.CharField(max_length=30,null=True)
    final_result = models.CharField(max_length=500,null=True,default='SOME STRING')
    file_size  = models.CharField(max_length=200,null=True)
    priority = models.IntegerField(null=True)

class devlog(models.Model):
    devid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class instances(models.Model):
    instance_name = models.CharField(max_length=20,unique=True,primary_key=True)
    algorithm = models.IntegerField()
    csvfile = models.CharField(max_length=20)
    timestamp = models.DateTimeField(null=True)


    
    class meta:
        db_table = "mcu"
        fields = "_all_"