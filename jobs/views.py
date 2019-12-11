from django.shortcuts import render
from .models import Job, Skills, Project, Social

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    skills = Skills.objects.all()
    projects = Project.objects.all()
    socials = Social.objects.all()
    context = {'jobs':jobs, 'skills':skills, 'projects':projects, 'socials':socials}
    return render(request, 'jobs/home.html', context)


