from django_prometheus.models import ExportModelOperationsMixin
from django.db import models

# Create your models here.

class Tasks(ExportModelOperationsMixin('task'), models.Model):
    task=models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id}:{self.task}"