from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    duedate = models.DateField()
    duetime = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'