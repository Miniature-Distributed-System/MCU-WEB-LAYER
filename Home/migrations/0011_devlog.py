# Generated by Django 4.1.3 on 2023-02-07 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_diagnosis_instance_disease_instance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='devlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devid', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
