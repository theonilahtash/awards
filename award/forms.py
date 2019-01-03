from django import forms
from .models import Profile, Project,Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AwardLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'post']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','posted_by']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['project','review']
