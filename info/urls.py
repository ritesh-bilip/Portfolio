from django.urls import path,include
from . import views


urlpatterns=[
  path('',views.index_page,name='index'),
  path('about/',views.about_page,name='about'),
  path('work/',views.work_page,name='work'),
  path('service/',views.services_page,name='service'),
  path('contact/',views.contact_page,name='contact')
]