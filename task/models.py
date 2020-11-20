from django.db import models
from django.contrib.auth.models import User

#email id unique
User._meta.get_field('email')._unique = True

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    address = models.CharField(max_length=2525)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'Profile for {self.user.username}'

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True,related_name='task_assigned_from')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True,related_name='task_assigned_for')
    date_time = models.DateTimeField()
    STATUS_CHOICES = (
      ('PENDING','Pending'),
      ('COMPLETED','Completed'),
    )
    status = models.CharField( max_length = 255, choices = STATUS_CHOICES, default = 'PENDING')


    def __str__(self):
        return f'Task for {self.assigned_to.username} from {self.assigned_by.username} '