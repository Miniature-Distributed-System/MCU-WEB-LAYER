# Generated by Django 4.2.1 on 2023-05-19 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0026_alter_instances_algorithm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instances',
            name='timestamp',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
