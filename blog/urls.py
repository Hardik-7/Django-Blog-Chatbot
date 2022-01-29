from django.contrib import admin
from django.urls import path
from  blog import views
import os

urlpatterns = [
    path("", views.home, name='home'),
    path("newspost/<int:id>/", views.newspost, name='newspost'),
    path("collagenews/", views.collagenews, name='collagenews'),
]
