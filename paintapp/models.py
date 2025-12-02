from django.db import models
from dashboard.models import *

# Create your models here.
class Uploadsave(models.Model):
    imagename=models.CharField(max_length=25,null=True,blank=True)
    description=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    uploadimage=models.ImageField(upload_to='uploadimages',null=True,blank=True)
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE,related_name='userdetails')

class Mycart(models.Model):
    art=models.ForeignKey(Uploadsave,on_delete=models.CASCADE)
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(null=True,blank=True,default=0)


class Whishlist(models.Model):
    art=models.ForeignKey(Uploadsave,on_delete=models.CASCADE)
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

# class Followers(models.Model):
#     following=models.ForeignKey(Customuser,on_delete=models.CASCADE)
#     follower=models.ForeignKey(Customuser,on_delete=models.CASCADE)
#     date=models.DateTimeField(auto_now_add=True)
