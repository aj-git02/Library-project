from django.shortcuts import render
from .models import Books,Borrow
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

def index1(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    x=Borrow.objects.filter(Issuer=request.user.username).filter(Onapproval=0)
    y=Borrow.objects.filter(Issuer=request.user.username).filter(Onapproval=1)
    return render(request,"books/index.html",{
        "books":Books.objects.all(),
        "approved":y,
        "unapproved":x
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
            #Books.objects.get(pk=book_id).issuers.add(Borrow.objects.get(Issuer=username))
            #Books.objects.get(pk=book_id).add(is)
            f=Borrow(Issuer=username,Name=y,Onapproval=0)
            f.save()
            return HttpResponseRedirect(reverse("index1"))
        else:
            return HttpResponseRedirect(reverse("index1"),{
                "message":"invalid credentials"
            })

def search(request):
    if request.method=="POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        x=Borrow.objects.filter(Issuer=request.user.username).filter(Onapproval=0)
        y=Borrow.objects.filter(Issuer=request.user.username).filter(Onapproval=1)
        details=Books.objects.filter(Name__icontains=request.POST["argument"])
        return render(request,"books/index.html",{
            "msg":details,
            "books":Books.objects.all(),
            "approved":y,
            "unapproved":x
        })
