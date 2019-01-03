from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Profile,Project,AwardLetterReciepients,Review
from .email import send_welcome_email
from .forms import AwardLetterForm,NewProfileForm,NewProjectForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from .permissions import IsAdminOrReadOnly




# Create your views here.
@login_required(login_url='/accounts/login')
def welcome(request):
    projects = Project.objects.all()
    print(projects)
    profile = Profile.objects.all()
    print(profile)
    # reviews = Review.objects.all()
    if request.method =='POST':
        form = AwardLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = AwardLetterReciepients(name = name,email = email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('index.html')
            print('valid')
    else:
        form = AwardLetterForm()

    return render(request, 'index.html',{"projects":projects,"profile":profile, "letterForm":form})

@login_required(login_url='/accounts/login/')
def add_review(request,pk):
    project = get_object_or_404(Project, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = form.save(commit=False)
            review.project = project
            review.juror = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.save()
            return redirect('welcome')
    else:
        form = ReviewForm()
        return render(request,'review.html',{"review-form":review-form})

@login_required(login_url='/accounts/login')
def profile(request,profile_id):
    profile = Profile.objects.get(pk = profile_id)
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
    return render(request,'new_profile.html', {"form":form})




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
    # project = project.objects.all()
    # print(project)
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return response(serializers.data)

    def post(self,request,format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.errors,status=status.Http_201_CREATED)
            return Response(serializers.errors,status=status.Http_400_BAD_REQUEST)

class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return response(serializers.data)

    def post(self,request,format=None):
        serializers = ProjectSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.errors,status=status.Http_201_CREATED)
            return Response(serializers.errors,status=status.Http_400_BAD_REQUEST)





