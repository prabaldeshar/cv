from django.shortcuts import render
from .models import Job, Skills, Project, Social, ProfileImage

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    skills = Skills.objects.all()
    projects = Project.objects.all()
    socials = Social.objects.all()
    profile_pic = ProfileImage.objects.all().first()
    context = {'jobs':jobs, 'skills':skills, 'projects':projects, 'socials':socials, 'profile_pic':profile_pic}
    return render(request, 'jobs/home.html', context)


