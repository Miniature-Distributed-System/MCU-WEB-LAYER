# Generated by Django 4.1.3 on 2023-03-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_devlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='active_instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_instance_id', models.CharField(max_length=20)),
                ('active_instance_name', models.CharField(max_length=20)),
                ('active_instance_type', models.CharField(max_length=20)),
                ('active_instance_col_no', models.IntegerField(max_length=2)),
                ('mandate_col1', models.CharField(max_length=10)),
                ('mandate_col2', models.CharField(max_length=10)),
            ],
        ),
    ]
