
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contactus/', views.contact_us, name='contact'),
    path('aboutus/', views.about_us, name='about'),
    path('payment/', views.payment, name='payment'),
    path('employee/', include("employee.urls")),
]