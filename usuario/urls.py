from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('create_user/', views.create_user, name='create_user'),
    path('profile/', views.profile, name='profile'),
]