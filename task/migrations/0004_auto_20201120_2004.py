# Generated by Django 3.1.3 on 2020-11-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20201120_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
