from django.urls import path
from . import views

urlpatterns = [
    path('workout/', views.workout, name='workout'),
    path('inf_workout/<int:id_exercise>/', views.inf_workout, name='inf_workout'),
]