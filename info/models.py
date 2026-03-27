# models.py
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title

class Feature(models.Model):
    service = models.ForeignKey(Service, related_name="features", on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
class Projects(models.Model):
    project_tag=models.CharField(max_length=50)
    project_title=models.CharField(max_length=100)
    project_intro=models.TextField
    live_demo = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_title

class Tech(models.Model):
    project = models.ForeignKey(Projects, related_name="techs", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Github(models.Model):
    repos=models.CharField(default='15+',max_length=1000)
    comit=models.CharField(default='300+',max_length=1000)
    stars=models.CharField(default='4+',max_length=1000)
    forks=models.CharField(default='0',max_length=1000)
    def __str__(self):
      return f"Repos: {self.repos}, Commits: {self.comit}"
   
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
