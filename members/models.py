from django.db import models
from django.utils.text import slugify

class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone =models.IntegerField(null=True)
    joined_data = models.DateField(null=True)
 

def __str__(self):
    return f"{self.firstname} {self.lastname}"