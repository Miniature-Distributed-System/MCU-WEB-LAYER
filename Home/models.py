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

    class meta:
        db_table = "mcu"

class diagnosis_instance(models.Model):
    diagnosis_id = models.CharField(max_length = 50)
    fever = models.CharField(max_length = 50)
    medicine = models.CharField(max_length = 50)
    filename= models.CharField(max_length=100)

class disease_instance(models.Model):
    disease_id = models.CharField(max_length = 50)
    fever = models.CharField(max_length=50)
    medicine = models.CharField(max_length=50)
    filename = models.CharField(max_length=100)

class devlog(models.Model):
    devid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class active_instance(models.Model):
    active_instance_id = models.CharField(max_length=20)
    active_instance_name = models.CharField(max_length=20)
    active_instance_type = models.CharField(max_length=20)
    active_instance_col_no = models.IntegerField(max_length=2)
    mandate_col1 = models.CharField(max_length=10)
    mandate_col2 = models.CharField(max_length=10)
    
    class meta:
        db_table = "mcu"