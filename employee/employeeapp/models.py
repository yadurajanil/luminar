from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.IntegerField()
    location=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images")
