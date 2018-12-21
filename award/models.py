from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(upload_to='profile/')
    phone = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    project_image = models.ImageField(upload_to='projects/',null=True)
    description = models.TextField(null=True)
    project_link = models.TextField(null=True)


    def get_projects(cls):
        projects = Project.objects.all()
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title_icontains=search_term)
        return projects

class AwardLetterReciepients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
