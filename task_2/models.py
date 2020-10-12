from __future__ import unicode_literals

from django.db import models
from auth_app.models import PMUser

# Create your models here.


class TaskDetails(models.Model):
    task_type = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(PMUser, on_delete=models.CASCADE)
    country =  models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "TaskDetails"
        verbose_name_plural = "TaskDetails"
