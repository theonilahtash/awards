from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.username


