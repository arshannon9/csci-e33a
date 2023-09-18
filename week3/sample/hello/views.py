from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def tony(request):
    return HttpResponse("Hello, Tony!")

def fergie(request):
    return HttpResponse("Hello, Fergie!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })