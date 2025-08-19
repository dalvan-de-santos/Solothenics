import re
from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db.models.functions import Lower
from django.db import IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProfileForm  
from .models import Profile
User = get_user_model()
USERNAME_RE = re.compile(r'^[a-zA-Z0-9_.-]{3,30}$')

def homepage(request):
    if request.user.is_authenticated:
        return redirect("profile")
    return render(request, 'homepage.html')
    


def create_user(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "GET":
        return render(request, 'usuario/create_user.html')
    
    elif request.method == "POST":
        username = request.POST.get("username").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        password2 = request.POST.get("password2").strip()

        errors = {}

        if not username: errors['username'] = "Username is required."
        if not email: errors['email'] = "Email is required."
        if not password: errors['password'] = "Password is required."
        
        if username and not USERNAME_RE.match(username):
            errors['username'] = "Use 3–30 caracteres (letras, números, ponto, underline ou hífen)."
        
        if email:
            try:
                EmailValidator()(email)
            except ValidationError:
                errors['email'] = "Email inválido."
        
        if password and password2 and password != password2:
            print("Passwords do not match")
            errors['password'] = "As senhas não coincidem."
        

        if password:
            try:
                temp_user = User(username=username, email=email)
                validate_password(password, user=temp_user)
            except ValidationError as e:
                print("Password validation error")
                errors['password'] = " ".join(e.messages)

        if username and User.objects.annotate(username_lower=Lower('username')).filter(username_lower=username.lower()).exists():
            errors['username'] = "Username já existe."

        if email and User.objects.annotate(email_lower=Lower('email')).filter(email_lower=email.lower()).exists():
            errors['email'] = "Email já existe."  
        
        if errors:
            return render(request, 'usuario/create_user.html', {"errors": errors, "values": {"username": username, "email": email}})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        except IntegrityError:
            messages.error(request, "Erro ao criar usuário. Tente novamente.")
            return redirect("create_user")
        
        login(request, user)
        return redirect("profile")


@login_required
def profile(request):
    if not request.user.is_authenticated:
        return redirect("login_user")

    profile = request.user.profile
    return render(request, 'usuario/profile.html', {"profile": profile})


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
        return render(request, 'usuario/login_user.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect("login_user")


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'usuario/edit_profile.html', {"form": form})


