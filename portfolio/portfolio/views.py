from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = {
        "name": "yash",
        "age": 12,
        "mob": 12234455,
        "friend":["a","d","f","g"]
    }
    return render(request,"index.html",data)
def about_us(request):
    data = "fetched data from db"
    return render(request,"about.html")

def contact_us(request):
    return render(request,"contactus.html")

def payment(request):
    return HttpResponse("payment page")