from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    sclass=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)