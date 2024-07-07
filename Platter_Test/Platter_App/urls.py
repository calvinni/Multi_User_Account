from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    #For login
    path('login/', views.Login, name='login'),
    path('login/checklogin/', views.check_login, name='check_login'),
    #For logout
    path('logout/', views.Logout, name='logout'),
    #For listing
    path('Acc/', views.List, name='list'),
    #For Register
    path('Create/', views.Register, name='register'),
    path('Create/CreateAcc/', views.CreateAcc, name='createAcc'),
]