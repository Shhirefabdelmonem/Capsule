from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def login(request):
    return render(request,"user/login.html")


def index(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/index.html', {'form': form})

def emptycart(request):
    return render(request, "user/emptycart.html")


def fullcart(request):
    return render (request, "user/fullcart.html")

def wish(request):
    return render (request, "user/wish.html")



# Create your views here.
