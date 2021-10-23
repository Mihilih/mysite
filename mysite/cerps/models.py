from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
    id=models.AutoField(primary_key=True)
    pass

class Jounral(models.Model):
    id=models.AutoField(primary_key=True)
    #name
    name=models.TextField(max_length=10000, blank=False, default="")
    #title
    title=models.TextField(max_length=10000, blank=False, default="")
    #authors
    #volume
    #issue
    #pages

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    #book/book chapter
    book_chap=models.TextField(max_length=10000, blank=False, default="")
    #book title
    book_title=models.TextField(max_length=10000, blank=False, default="")
    #chapter title
    chap_title=models.TextField(max_length=10000, blank=False, default="")
    #authors
    #year
    #publisher
    isbn=models.TextField(max_length=10000, blank=False, default="")
    #ISBN

class Patent(models.Model):
    id=models.AutoField(primary_key=True)
    #filing agency
    agency=models.TextField(max_length=10000, blank=False, default="")
    #title
    title=models.TextField(max_length=10000, blank=False, default="")
    #number
    #authors
    #year

class Grant(models.Model):
    id=models.AutoField(primary_key=True)
    #funding agency
    agency=models.TextField(max_length=10000, blank=False, default="")
    #title
    title=models.TextField(max_length=10000, blank=False, default="")
    #name of PI
    pi=models.TextField(max_length=10000, blank=False, default="")
    #co-inversigators
    #budgets
    #duration

class Award(models.Model):
    id=models.AutoField(primary_key=True)
    #name
    name=models.TextField(max_length=10000, blank=False, default="")
    #award
    award=models.TextField(max_length=10000, blank=False, default="")
    #awarding agency
    agency=models.TextField(max_length=10000, blank=False, default="")
    #year