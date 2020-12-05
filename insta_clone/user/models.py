from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager
from user.manager import CustomUserManager

# Create your models here.
# AbstractUser to change in exiting user
class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures',null=False,blank=False)
    full_name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    #remove pre defined fields
    first_name = None
    last_name= None

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['full_name',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email