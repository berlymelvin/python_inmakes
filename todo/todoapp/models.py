from django.db import models

# Create your models here.

class Todo(models.Model):
    item=models.TextField()
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.item
