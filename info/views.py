from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .serializers import *
from rest_framework import generics,viewsets 
from django.contrib import messages
#?------Api viset-------
# Create your views here.
class ProfileView(viewsets.ModelViewSet):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
class SkillView(viewsets.ModelViewSet):
   queryset=Skill.objects.all()
   serializer_class=SkillSerializer
class ProjectView(viewsets.ModelViewSet):
   queryset=Project.objects.all()
   serializer_class=ProjectSerializer
class EducationVIew(viewsets.ModelViewSet):
   queryset=Education.objects.all()
   serializer_class=EducationSerializer
class CertificationView(viewsets.ModelViewSet):
   queryset=Certification.objects.all()
   serializer_class=CertificationSerializer
class ContactView(generics.CreateAPIView):
   serializer_class=ContactMessageSerializer


#?------ Django Template Views -------
def index_page(request):
    profile = Profile.load()
    return render(request, 'index.html', {'profile': profile})

def about_page(request):
    profile = Profile.load()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    return render(request, 'about.html', {
        'profile': profile,
        'education': education,
        'certifications': certifications,
    })

def work_page(request):
    projects = Project.objects.all()
    return render(request, 'work.html', {'projects': projects})

def service_page(request):
    skills = Skill.objects.all()
    grouped_skills = {}
    for skill in skills:
        cat = skill.get_category_display()
        grouped_skills.setdefault(cat, []).append(skill)
    return render(request, 'service.html', {'grouped_skills': grouped_skills})

def contact_page(request):
    profile = Profile.load()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form, 'profile': profile})