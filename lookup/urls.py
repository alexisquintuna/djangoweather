#this is my views.py file
from django.urls import path
from . import views

#anytime we add a new webpage it goes in here
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]

