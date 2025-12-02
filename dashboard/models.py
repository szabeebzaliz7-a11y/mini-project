from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customuser(AbstractUser):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    password=models.CharField(max_length=25,null=True,blank=True)
    