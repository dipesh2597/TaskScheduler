# Generated by Django 3.1.3 on 2020-11-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING', max_length=255),
        ),
    ]
