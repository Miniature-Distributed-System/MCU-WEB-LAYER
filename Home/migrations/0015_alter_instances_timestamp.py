# Generated by Django 4.1.3 on 2023-03-13 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_delete_diagnosis_instance_delete_disease_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instances',
            name='timestamp',
            field=models.CharField(max_length=30),
        ),
    ]
