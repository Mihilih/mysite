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
    if request.method == "PUT":
        name=request.POST['name']
        title=request.POST['title']
        authors=request.POST['authors']
        authlist=[x.strip() for x in authors.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append[person]
            except People.DoesNotExist:
                person=People()
                person.name=x;
                person.save()
                per=People.objects.get(name=x)
                auth.append[person]
        volume=request.POST['volume']
        issue=request.POST['issue']
        pages=request.POST['pages']
        jounal=Jounral()
        journal.name=name
        journal.title=title
        journal.volume=volume
        journal.issue=issue
        journal.pages=pages
        journal.save()
        for x in auth:
            jounal.authors.add(x)
        journal.save()
        return render(request, "cerps/journaladd.html")
    else:
        return render(request, "cerps/journaladd.html")

#add and display book
def book(request):
    if request.method == "PUT":
        pass
    else:
        return render(request, "cerps/bookadd.html")

#add and display patent
def patent(request):
    if request.method == "PUT":
        pass
    else:
        return render(request, "cerps/patentadd.html")

#add and display grant
def grant(request):
    if request.method == "PUT":
        pass
    else:
        return render(request, "cerps/grantadd.html")

#add and display award
def award(request):
    if request.method == "PUT":
        pass
    else:
        return render(request, "cerps/awardadd.html")