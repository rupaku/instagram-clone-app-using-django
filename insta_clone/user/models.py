from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures',null=False,blank=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =[]

    # objects = BaseUserManager()
