from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.about_us, name='about'),
    path('payment/', views.payment, name='payment'),
    ]