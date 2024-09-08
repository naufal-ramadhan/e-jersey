from django.shortcuts import render,get_object_or_404
from .models import Jersey

# Create your views here.
def home(request):
    context = {
        "title" : "Home",
    }

    return render(request, "main.html", context)

def clubSelection(request):
    jerseys = Jersey.objects.filter(type="club")
    context = {
        "title" : "Selection",
        "type" : "Club Jersey",
        "jerseys" : jerseys
    }
    return render(request, "selection.html", context)

def nationalSelection(request):
    jerseys = Jersey.objects.filter(type="national")
    context = {
        "title" : "Selection",
        "type" : "National Jersey",
        "jerseys" : jerseys
    }
    return render(request, "selection.html", context)

def viewJersey(request, type, slug):
    jersey = Jersey.objects.get(slug=slug)
    context = {
        "title" : "Jersey",
        "type" : "Jersey",
        "jersey" : jersey
    }
    return render(request, "view.html", context)