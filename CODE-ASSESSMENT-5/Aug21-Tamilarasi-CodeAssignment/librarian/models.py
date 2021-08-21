from django.db import models

# Create your models here.
class Librarian(models.Model):
    enroll_code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mblno=models.BigIntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=50)