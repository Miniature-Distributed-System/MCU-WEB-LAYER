# Generated by Django 4.1.3 on 2023-03-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_active_instance'),
    ]

    operations = [
        migrations.CreateModel(
            name='instances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_name', models.CharField(max_length=20, unique=True)),
                ('algorithm', models.CharField(max_length=20)),
                ('csvfile', models.CharField(max_length=20)),
                ('timestamp', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='active_instance',
        ),
    ]
