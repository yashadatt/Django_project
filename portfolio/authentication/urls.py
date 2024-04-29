from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.authlogin, name='login'),
    path('registration/', views.authregistration, name='registration'),
    path('forget-password', views.forget_password, name='forget_password'),
    path('logout/', views.auth_logout, name='logout'),

]