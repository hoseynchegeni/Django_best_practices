from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser , PermissionsMixin
from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length= 255, unique= True)
    is_superuser = models.BooleanField(default= False)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    # is_verified =  models.BooleanField(default= False)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    image = models.ImageField(blank= True, null= True)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.user.email

@receiver(post_save, sender = User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
