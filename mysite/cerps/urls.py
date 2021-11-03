from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("view", views.view, name="view"),
    path("journal", views.journal, name="journal"),
    path("book", views.book, name="book"),
    path("patent", views.patent, name="patent"),
    path("grant", views.grant, name="grant"),
    path("award", views.award, name="award"),
]