from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "cerps/index.html")

def add(request):
    return render(request, "cerps/add.html")

#add and display journal
def journal(request):
    if request.method == "PUT":
        pass
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