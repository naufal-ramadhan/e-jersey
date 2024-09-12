from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.
def dataDiri(request):
    context = {
        "nama" : "Muhammad Naufal Ramadhan",
        "npm" : "2306241700",
        "kelas" : "D",
    }
    return render(request, "dataDiri.html", context)

