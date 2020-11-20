# Generated by Django 3.1.3 on 2020-11-20 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[(0, 'Pending'), (1, 'Completed')], default=0, max_length=2)),
                ('assigned_by', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='task_assigned_from', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='task_assigned_for', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]