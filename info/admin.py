# admin.py
from django.contrib import admin
from .models import Service, Feature,Projects,Tech,Github

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [FeatureInline]

class TechInline(admin.TabularInline):
    model = Tech
    extra = 1

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechInline]
admin.site.register(Github)