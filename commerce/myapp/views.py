from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def project(request):
    return render(request,'project.html')

def Experiences(request):
    return render(request,'Experiences.html')

def Resume(request):
    return render(request,'Resume.html')

