from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import templates

# Create your views here.
def index(request):
    if not request.users.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")

def login_view(request):
    if request.method=="POST":
        username=request.POST("Username")
        password=request.POST("Password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{
                "message":"invalid credentials"
            })
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"logged out"
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

# Create your views here.
