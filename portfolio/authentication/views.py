from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request,"Invalid email or password broo try again")
    return render(request, 'authentication/login.html')

def auth_logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out...")
    return redirect('login')

def authregistration(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if confirm_password== password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exist.. try another username")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email is already registered...")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request, "Successfully registered user...")
                return redirect('login')
        else:
            messages.success(request, "Password and confirm password doesnot match...")
    return render(request, 'authentication/register.html')


def forget_password(request):
    return render(request, 'authentication/forget.html')
