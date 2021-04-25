from django.urls import path
from . import views
urlpatterns = [
    path("",views.index1,name="index1"),
    path("<int:book_id>",views.book,name="book"),
    path("<int:book_id>/issue",views.issue,name="issue"),
]