from django.shortcuts import render
from .models import Books

def index(request):
    return render(request,"books/index.html",{
        "books":Books.objects.all()
    })

def book(request,book_id):
    book=Books.objects.get(pk=book_id)
    return render(request,"books/book.html",{
        "book":book
    })
