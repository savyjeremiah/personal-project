from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('about/',views.about,name='about'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('project/',views.project,name='project'),
    path('Experiences/',views.Experiences,name='Experiences'),
    path('Resume/',views.Resume,name='Resume'),
   
    
]