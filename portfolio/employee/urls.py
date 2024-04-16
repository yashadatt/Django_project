
from django.urls import path,include
from . import views
urlpatterns = [
    path('new/', views.employee_details),
    path('profile/', views.employee_details,name='profile'),
]