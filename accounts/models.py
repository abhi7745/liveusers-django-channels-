# This Django app is build for automation using python, build by Abhijith KR 

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class User_Account(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.user_id.username
    


class TotalUsers_realtime(models.Model):
    ip_address = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.ip_address
    
