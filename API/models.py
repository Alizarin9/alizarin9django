from django.db import models

class task_data(models.Model):
    task_type = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    deadline = models.CharField(max_length=40)

    def __str__(self):
        return self.task_type