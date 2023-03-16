# Generated by Django 4.1.3 on 2023-01-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_filelog_algorithm'),
    ]

    operations = [
        migrations.CreateModel(
            name='candidate_algo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sky', models.CharField(max_length=10)),
                ('temperature', models.CharField(max_length=10)),
                ('humid', models.CharField(max_length=10)),
                ('wind', models.CharField(max_length=10)),
                ('water', models.CharField(max_length=10)),
                ('forecast', models.CharField(max_length=10)),
                ('output', models.CharField(max_length=10)),
                ('filename', models.CharField(max_length=10)),
            ],
        ),
    ]
