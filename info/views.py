from django.shortcuts import render,redirect
from .models import Service,Projects,Github
from .forms import ContactForm
# Create your views here.

def index_page(request):
  return render(request,'portfolio/index.html')
def about_page(request):
  return render(request,'portfolio/about.html')
def work_page(request):
    projects = Projects.objects.all()
    stats = Github.objects.all()
    return render(request, 'portfolio/work.html', {
      "projects": projects,
      "stats": stats
    })
def services_page(request):
    services = Service.objects.all()
    return render(request, 'portfolio/services.html', {"services": services})
def contact_page(request):
  return render(request,'portfolio/contact.html')
def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {"form": form})
