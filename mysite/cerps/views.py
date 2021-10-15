from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "cerps/index.html")

def downloads(request):
    return render(request, "cerps/downloads.html")
