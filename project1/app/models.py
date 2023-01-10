from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Services(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    icon=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class Teams(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    icon=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name