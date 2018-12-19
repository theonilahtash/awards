from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.
def welcome(request):
    # award = projects.objects.all()
    return render(request, 'index.html')


