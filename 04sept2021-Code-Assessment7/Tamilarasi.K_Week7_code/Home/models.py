from django.db import models

# Create your models here.
class home(models.Model):
    name=models.CharField(max_length=40,default='',blank=True)
    username=models.CharField(max_length=40,default='',blank=True)
    password = models.CharField(max_length=40, default='', blank=True)
