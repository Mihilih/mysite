import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from cerps.models import *

# Create your views here.
def index(request):
    return render(request, "cerps/index.html")

def add(request):
    return render(request, "cerps/add.html")

#add and display journal
def journal(request):
    if request.method == "POST":
        name=request.POST['name']
        title=request.POST['title']
        authors=request.POST['authors']
        authlist=[x.strip() for x in authors.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)
        volume=request.POST['volume']
        issue=request.POST['issue']
        pages=request.POST['pages']

        journal=Journal()
        journal.name=name
        journal.title=title
        journal.volume=volume
        journal.issue=issue
        journal.pages=pages
        journal.save()
        for x in auth:
            journal.authors.add(x)
        journal.save()
        return render(request, "cerps/journaladd.html")
    else:
        return render(request, "cerps/journaladd.html")

#add and display book
def book(request):
    if request.method == "POST":
        chap=request.POST['chap']
        book_title=request.POST['book_title']
        chap_title=request.POST['chap_title']
        authors=request.POST['authors']
        authlist=[x.strip() for x in authors.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)
        isbn=request.POST['isbn']
        year=request.POST['year']
        publisher=request.POST['publisher']

        book=Book()
        book.book_chap=chap
        book.book_title=book_title
        book.chap_title=chap_title
        book.year=year
        book.isbn=isbn
        book.publisher=publisher
        book.save()
        for x in auth:
            book.authors.add(x)
        book.save()
        return render(request, "cerps/bookadd.html")
    else:
        return render(request, "cerps/bookadd.html")

#add and display patent
def patent(request):
    if request.method == "POST":
        agency=request.POST['agency']
        title=request.POST['title']
        number=request.POST['number']
        authors=request.POST['authors']
        authlist=[x.strip() for x in authors.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)

        year=request.POST['year']
        patent=Patent()
        patent.agency=agency
        patent.title=title
        patent.number=number
        patent.year=year
        patent.save()
        for x in auth:
            patent.authors.add(x)
        patent.save()
        return render(request, "cerps/patentadd.html")
    else:
        return render(request, "cerps/patentadd.html")

#add and display grant
def grant(request):
    if request.method == "POST":
        agency=request.POST['agency']
        title=request.POST['title']
        pi=request.POST['pi']
        co_investigators=request.POST['investigators']
        authlist=[x.strip() for x in co_investigators.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)

        grant=Grant()
        grant.agency=agency
        grant.title=title
        grant.pi=pi
        grant.save()
        for x in auth:
            grant.co_investigators.add(x)
        grant.save()
        return render(request, "cerps/grantadd.html")
    else:
        return render(request, "cerps/grantadd.html")

#add and display award
def award(request):
    if request.method == "POST":
        name=request.POST['name']
        award_title=request.POST['award']
        agency=request.POST['agency']
        year=request.POST['year']
        
        award=Award()
        award.name=name
        award.award=award_title
        award.agency=agency
        award.year=year
        award.save()
        return render(request, "cerps/awardadd.html")
        pass
    else:
        return render(request, "cerps/awardadd.html")