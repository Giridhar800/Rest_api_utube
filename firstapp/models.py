from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    fathername = models.CharField(max_length=20)
    
