from django.contrib import admin
from .models import Exercise, BeginnerExercise, IntermediateExercise, AdvancedExercise, PersonalizedTraining, WorkoutPlan

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'muscle_group')
    search_fields = ('name', 'category', 'muscle_group')
    list_filter = ('category', 'muscle_group')



@admin.register(BeginnerExercise)
class BeginnerExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_id', 'difficulty', 'repetitions', 'sets')
    search_fields = ('exercise_id__name', 'difficulty')
    list_filter = ('difficulty',)

@admin.register(IntermediateExercise)
class IntermediateExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_id', 'difficulty', 'repetitions', 'sets')
    search_fields = ('exercise_id__name', 'difficulty')
    list_filter = ('difficulty',)

@admin.register(AdvancedExercise)
class AdvancedExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_id', 'difficulty', 'repetitions', 'sets')
    search_fields = ('exercise_id__name', 'difficulty')
    list_filter = ('difficulty',)

@admin.register(PersonalizedTraining)
class PersonalizedTrainingAdmin(admin.ModelAdmin):
    list_display = ('user', 'difficulty', 'repetitions', 'sets')
    search_fields = ('user__username', 'difficulty')
    list_filter = ('difficulty',)

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'duration', 'frequency')
    search_fields = ('user__username',)
    list_filter = ('frequency',)
