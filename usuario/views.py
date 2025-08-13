from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def homepage(request):
    if request.user.is_authenticated:
        return redirect("profile")
    return render(request, 'homepage.html')


def create_user(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "GET":
        return render(request, 'create_user.html')
    
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            return HttpResponse("Username already exists.")
        
        user = User.objects.filter(email=email)
        if user.exists():
            return HttpResponse("Email already exists.")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect("profile")


@login_required
def profile(request):
    return render(request, 'profile.html')



def login_user(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("profile")
        else:
            return HttpResponse("Invalid credentials.")
    else:
        form = AuthenticationForm()
        return render(request, 'login_user.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect("login_user")