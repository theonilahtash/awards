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

    return render(request, 'index.html',{"letterForm":form})

@login_required(login_url='/accounts/login')
def profile(request,profile_id):
    profile = Profile.objects.get(pk = profile_id)
    print(Profile)
    projects = Project.get_all()
    return render(request,'profile.html',{"profile":profile,"projects":projects})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')
    else:
        form = NewProfileForm()
    return render(request,'new_profile.html', {"profile_form":profile_form})




def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-award/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "Searched"
        return render(request, 'all-award/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    project = project.objects.all()
    print(project)
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


