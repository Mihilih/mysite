from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    #add and display journal
    #add and display book
    #add and display patent
    #add and display grant
    #add and display award
]