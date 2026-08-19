# admin.py
from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(ContactMessage)