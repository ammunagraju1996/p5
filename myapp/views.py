from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def trail(request):
    return HttpRequest("<h1>project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
     return render(request,"myapp/home.html")

def profile(request):
    name="archana"
    return render(request,"myappp/profile.html",{'name':name})