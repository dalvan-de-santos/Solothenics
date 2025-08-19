from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import BeginnerExercise

@login_required
def workout(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    
    if request.user.profile.rank == "E" or request.user.profile.rank == "D":
        exercises = BeginnerExercise.objects.all()

    return render(request, 'workout.html', {"exercises": exercises})


def inf_workout(request,id_exercise):

    if not request.user.is_authenticated:
        return redirect("login_user")

    if request.user.profile.rank == "E" or request.user.profile.rank == "D":
        exercise = BeginnerExercise.objects.get(id=id_exercise)
    return render(request, 'info_workout.html', {"exercise": exercise})
