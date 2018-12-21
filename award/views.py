from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Profile,Project,AwardLetterReciepients
from .email import send_welcome_email
from .forms import AwardLetterForm
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='/accounts/login')
def welcome(request):
    projects = Project.objects.all()
    if request.method =='POST':
        form = AwardLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = AwardLetterReciepients(name = name,email = email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('welcome.html')
            print('valid')
    else:
        form = AwardLetterForm()

    return render(request, 'index.html',{"projects":projects,"letterForm":form})

@login_required(login_url='/accounts/login')
def profile(request,profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-award/profile.html",{"profile":profile})

    
   

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-award/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "Searched"
        return render(request, 'all-award/search.html',{"message":message})