# Generated by Django 4.2.1 on 2023-05-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0022_rename_upload_time_filelog_timestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='userid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
