from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    publisher=models.CharField(max_length=20)
    price=models.IntegerField()