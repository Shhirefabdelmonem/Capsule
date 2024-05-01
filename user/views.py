from django.shortcuts import render

def login(request):
    return render(request,"user/login.html")


def index(request):
    return render(request, "user/index.html")

def emptycart(request):
    return render(request, "user/emptycart.html")


def fullcart(request):
    return render (request, "user/fullcart.html")

def wish(request):
    return render (request, "user/wish.html")



# Create your views here.
