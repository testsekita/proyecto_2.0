from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    allplatillos = platillos.objects.all()
    return render(request, 'index.html', {'allplatillos':allplatillos})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def elements(request):
    return render(request, 'elements.html')

def menu(request):
    return render(request, 'menu.html')
