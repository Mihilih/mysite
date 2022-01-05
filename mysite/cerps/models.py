from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class User(AbstractUser):
    id=models.AutoField(primary_key=True)
    pass

class People(models.Model):
    id=models.AutoField(primary_key=True)
    name=TextField(max_length=10000, blank=False, default="")
    def __str__(self):
        return f"{self.name}"

class Journal(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=10000, blank=False, default="")
    title=models.TextField(max_length=10000, blank=False, default="")
    authors=models.ManyToManyField("People", related_name="journal")
    volume=models.IntegerField(blank=False, default=0)
    issue=models.IntegerField(blank=False, default=0)
    pages=models.TextField(max_length=10000, blank=False, default="")

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    book_bool=models.BooleanField(blank=False)#book/book chapter
    book_title=models.TextField(max_length=10000)
    chapter_title=models.TextField(max_length=10000)
    authors=models.ManyToManyField("People", related_name="book")
    year=models.IntegerField(blank=False, default=0)
    publisher=models.TextField(max_length=10000, blank=False, default="")
    isbn=models.TextField(max_length=10000, blank=False, default="")
    

class Patent(models.Model):
    id=models.AutoField(primary_key=True)
    agency=models.TextField(max_length=10000, blank=False, default="")#filing agency
    title=models.TextField(max_length=10000, blank=False, default="")
    number=models.IntegerField(blank=False, default=0)
    authors=models.ManyToManyField("People", related_name="patent")
    year=models.IntegerField(blank=False, default=0)

class Grant(models.Model):
    id=models.AutoField(primary_key=True)
    agency=models.TextField(max_length=10000, blank=False, default="")#funding agency
    title=models.TextField(max_length=10000, blank=False, default="")
    pi=models.TextField(max_length=10000, blank=False, default="")#name of PI
    co_investigators =models.ManyToManyField("People", related_name="grant")
    budget=models.IntegerField(blank=False, default=0)
    duration_from=models.DateField(blank=False, default=0)
    duration_to=models.DateField(blank=False, default=0)

class Award(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=10000, blank=False, default="")
    award=models.TextField(max_length=10000, blank=False, default="")
    agency=models.TextField(max_length=10000, blank=False, default="")#awarding agency
    year=models.IntegerField(blank=False, default=0)