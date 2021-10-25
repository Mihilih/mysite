from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.core.validators import MaxValueValidator

# Create your models here.
class User(AbstractUser):
    id=models.AutoField(primary_key=True)
    pass

class People(models.Model):
    id=models.AutoField(primary_key=True)
    name=TextField(max_length=10000, blank=False, default="")

class Jounral(models.Model):
    id=models.AutoField(primary_key=True)
    #name
    name=models.TextField(max_length=10000, blank=False, default="")
    #title
    title=models.TextField(max_length=10000, blank=False, default="")
    #authors
    authors=models.ManyToManyField("People", related_name="journal")
    #volume
    volume=models.IntegerField(blank=False, default=0)
    #issue
    issue=models.IntegerField(blank=False, default=0)
    #pages
    pages=models.IntegerField(blank=False, default=0)

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    #book/book chapter
    book_chap=models.TextField(max_length=10000, blank=False, default="")
    #book title
    book_title=models.TextField(max_length=10000, blank=False, default="")
    #chapter title
    chap_title=models.TextField(max_length=10000, blank=False, default="")
    #authors
    authors=models.ManyToManyField("People", related_name="book")
    #year
    year=models.IntegerField(blank=False, default=0)
    #publisher
    publisher=models.TextField(max_length=10000, blank=False, default="")
    #ISBN
    isbn=models.TextField(max_length=10000, blank=False, default="")
    

class Patent(models.Model):
    id=models.AutoField(primary_key=True)
    #filing agency
    agency=models.TextField(max_length=10000, blank=False, default="")
    #title
    title=models.TextField(max_length=10000, blank=False, default="")
    #number
    number=models.IntegerField(blank=False, default=0)
    #authors
    authors=models.ManyToManyField("People", related_name="patent")
    #year
    year=models.IntegerField(blank=False, default=0)

class Grant(models.Model):
    id=models.AutoField(primary_key=True)
    #funding agency
    agency=models.TextField(max_length=10000, blank=False, default="")
    #title
    title=models.TextField(max_length=10000, blank=False, default="")
    #name of PI
    pi=models.TextField(max_length=10000, blank=False, default="")
    #co-inversigators
    co_investigators =models.ManyToManyField("People", related_name="grant")
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
    year=models.IntegerField(blank=False, default=0)