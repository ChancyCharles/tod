from django.db import models

# Create your models here.
class Todo(models.Model):
    Task = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Deadline = models.DateTimeField()
    def __str__(self):
        return self.Task