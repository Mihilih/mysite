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
    #title
    #authors
    #volume
    #issue
    #pages

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    #book/book chapter
    #book title
    #chapter title
    #authors
    #year
    #publisher
    #ISBN

class Patent(models.Model):
    id=models.AutoField(primary_key=True)
    #filing agency
    #title
    #number
    #authours
    #year

class Grant(models.Model):
    id=models.AutoField(primary_key=True)
    #funding agency
    #title
    #name if PI
    #co-inversigators
    #budgets
    #duration

class Award(models.Model):
    id=models.AutoField(primary_key=True)
    #name
    #award
    #awarding agency
    #year