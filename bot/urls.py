from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
   
    path("", views.home, name='home'),
   
    path("search", views.search, name='search'),
    #path("news", views.news, name='news'),
    path("Contact", views.Contact, name='Contact'),
    #path("answer", views.answer, name="answer"),
]
