# Generated by Django 4.2.1 on 2023-05-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0024_alter_filelog_aliasname_alter_filelog_file_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instances',
            name='algorithm',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='instances',
            name='timestamp',
            field=models.TimeField(),
        ),
    ]
