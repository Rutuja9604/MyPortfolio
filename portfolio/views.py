from django.shortcuts import render, redirect
from .models import About, Skill, Project, Contact, Education, Certification

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    about_data = About.objects.first()
    return render(request, 'portfolio/about.html', {'about': about_data})

def skills(request):
    skills_data = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skills_data})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('contact')

    return render(request, 'portfolio/contact.html')


def education(request):
    education_list = Education.objects.all()
    certifications = Certification.objects.all()
    return render(request, 'portfolio/education.html', {
        'education_list': education_list,
        'certifications': certifications
    })
