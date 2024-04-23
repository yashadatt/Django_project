from django.shortcuts import render
from django.http import HttpResponse
from .models import About,Slider,Client

def home(request):
    about_data = About.objects.all()
    print(about_data[0].title)
    slider_data = Slider.objects.all()
    print(slider_data[0].title)
    client_data = Client.objects.all()

    context = {
        "about_data": about_data,
        "slider_data": slider_data,
        "client_data": client_data
    }
    return render(request, "index.html", context)


def about_us(request):
    return render(request,"about.html")


def payment(request):
    return HttpResponse("payment page")