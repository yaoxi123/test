from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=40)
  sex = models.CharField(max_length=10)
  age = models.IntegerField()
  isdelete = models.BooleanField(default=False)
