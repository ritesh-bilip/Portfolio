from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# Router for DRF API endpoints
router = DefaultRouter()
router.register('profile', views.ProfileView, basename='api-profile')
router.register('skills', views.SkillView, basename='api-skill')
router.register('projects', views.ProjectView, basename='api-project')
router.register('education', views.EducationVIew, basename='api-education')
router.register('certifications', views.CertificationView, basename='api-certifications')


urlpatterns = [
    # Template Page Routes
    path('', views.index_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('work/', views.work_page, name='work'),
    path('service/', views.service_page, name='service'),
    path('contact/', views.contact_page, name='contact'),

    # API Routes (Future Use)
    path('api/', include(router.urls)),
    path('api/contact/', views.ContactView.as_view(), name='api-contact'),
]