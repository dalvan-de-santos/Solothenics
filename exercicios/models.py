from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Exercício')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    category = models.CharField(max_length=50, verbose_name='Categoria')
    muscle_group = models.CharField(max_length=50, verbose_name='Grupo Muscular')

    class Meta:
        verbose_name = 'Exercício'
        verbose_name_plural = 'Exercícios'

    def __str__(self):
        return self.name


class BeginnerExercise(models.Model):
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='beginner_exercises', verbose_name='Exercício')
    difficulty = models.CharField(max_length=50, default='Beginner', verbose_name='Dificuldade')
    repetitions = models.IntegerField(default=6, verbose_name='Repetições')
    sets = models.IntegerField(default=3, verbose_name='Séries')

    class Meta:
        verbose_name = 'Exercício Iniciante'
        verbose_name_plural = 'Exercícios Iniciantes'

    def __str__(self):
        return f"{self.exercise_id.name} - {self.difficulty}"
    

class IntermediateExercise(models.Model):
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='intermediate_exercises', verbose_name='Exercício')
    difficulty = models.CharField(max_length=50, default='Intermediate', verbose_name='Dificuldade')
    repetitions = models.IntegerField(default=15, verbose_name='Repetições')
    sets = models.IntegerField(default=5, verbose_name='Séries')

    class Meta:
        verbose_name = 'Exercício Intermediário'
        verbose_name_plural = 'Exercícios Intermediários'

    def __str__(self):
        return f"{self.exercise_id.name} - {self.difficulty}"


class AdvancedExercise(models.Model):
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='advanced_exercises', verbose_name='Exercício')
    difficulty = models.CharField(max_length=50, default='Advanced', verbose_name='Dificuldade')
    repetitions = models.IntegerField(default=20, verbose_name='Repetições')
    sets = models.IntegerField(default=6, verbose_name='Séries')

    class Meta:
        verbose_name = 'Exercício Avançado'
        verbose_name_plural = 'Exercícios Avançados'

    def __str__(self):
        return f"{self.exercise_id.name} - {self.difficulty}"


class PersonalizedTraining(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personalized_trainings', verbose_name='Usuário')
    exercises = models.ManyToManyField(Exercise, verbose_name='Exercícios')
    difficulty = models.CharField(max_length=50, default='Advanced', verbose_name='Dificuldade')
    repetitions = models.IntegerField(default=0, verbose_name='Repetições')
    sets = models.IntegerField(default=0, verbose_name='Séries')


    class Meta:
        verbose_name = 'Treino Personalizado'
        verbose_name_plural = 'Treinos Personalizados'

    def __str__(self):
        return f"Treino Personalizado - {self.user.username}"


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans', verbose_name='Usuário')
    exercises = models.ManyToManyField(Exercise, verbose_name='Exercícios')
    duration = models.IntegerField(default=0, verbose_name='Duração (minutos/repetições)')
    frequency = models.CharField(max_length=50, default='3 vezes por semana', verbose_name='Frequência')

    class Meta:
        verbose_name = 'Plano de Treino'
        verbose_name_plural = 'Planos de Treino'

    def __str__(self):
        return f"Plano de Treino - {self.user.username}"
