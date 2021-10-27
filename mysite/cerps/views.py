from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "cerps/index.html")

def add(request):
    return render(request, "cerps/add.html")

#add and display journal
#add and display book
#add and display patent
#add and display grant
#add and display award