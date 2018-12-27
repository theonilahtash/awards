from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='profile_image',blank=True)
    phone = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    # def create_profile(sender,**kwargs):
    #     if kwargs['created']:
    #         user_profile = Profile.objects.create(User*kwargs['instance'])
    # post_save.connect(create_profile,sender=User)

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles



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

class Review(models.Model):
    review = models.TextField(blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='reviews',null=True)
    design = models.IntegerField(choices=RATING_CHOICES,default=0)
    usability = models.IntegerField(choices=RATING_CHOICES,default=0)
    content = models.IntegerField(choices=RATING_CHOICES,default=0)

    @classmethod
    def get_reviews(cls):
        reviews = Reviews.objects.all()
        return reviews
