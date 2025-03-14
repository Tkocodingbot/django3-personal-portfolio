from django.shortcuts import render
from .models import project

def home(request):
    Project = project.objects.all()
    return render(request, 'portfolio/home.html', {'Project':Project})


