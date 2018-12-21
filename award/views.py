from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Profile,Project,AwardLetterReciepients
from .email import send_welcome_email
from .forms import AwardLetterForm



# Create your views here.
def welcome(request):
    projects = Project.objects.all()
    if request.method =='POST':
        form = AwardLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = AwardLetterRecipients(name = name,email = email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('welcome.html')
            print('valid')
    else:
        form = AwardLetterForm()

    return render(request, 'index.html',{"projects":projects,"letterForm":form})


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