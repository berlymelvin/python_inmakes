from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.TextField()
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='thumb')

    def __str__(self):
        return self.name
