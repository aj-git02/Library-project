from django.shortcuts import render
from .models import Books,Borrow
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

def index1(request):
    return render(request,"books/index.html",{
        "books":Books.objects.all()
    })

def book(request,book_id):
    b=Books.objects.get(pk=book_id)
    return render(request,"books/book.html",{
        "book":b
    })

def issue(request,book_id):
    if request.method=="POST":
        y=Books.objects.get(pk=book_id)
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            x=Borrow.objects.get(Issuer=username)
            y=Books.objects.get(pk=book_id)
            y.issuers.add(x)
            return HttpResponseRedirect(reverse("index1"))
        else:
            return HttpResponseRedirect(reverse("index1"),{
                "message":"invalid credentials"
            })
        