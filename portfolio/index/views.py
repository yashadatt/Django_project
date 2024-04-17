from django.shortcuts import render
from django.http import HttpResponse
from .models import About

def home(request):
    about_data = About.objects.all()
    print(about_data[0].title)
    context={
        "about_data":about_data
    }
    return render(request, "index.html", context)


def about_us(request):
    return render(request,"about.html")


def contact_us(request):
    return render(request,"contactus.html")


def payment(request):
    return HttpResponse("payment page")