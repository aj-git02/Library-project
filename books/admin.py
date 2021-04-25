from django.contrib import admin

# Register your models here.
from .models import Books,Borrow
admin.site.register(Books)
admin.site.register(Borrow)