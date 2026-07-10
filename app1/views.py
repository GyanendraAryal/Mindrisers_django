from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome this is index page!")

def home(request):
    return HttpResponse("I'm from the Home Page")

def contact(request):
    return HttpResponse("I'm from contact page")

def userinfo(request):
    return render(request,"index.html")