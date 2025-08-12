from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile', verbose_name='Usuário')
    bio = models.TextField(blank=True, null=True, verbose_name='Biografia')
    profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m', blank=True, null=True, verbose_name='Foto do Perfil')
    level = models.CharField(max_length=50, default='Beginner', verbose_name='Nível')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class PhysicalAssessment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='physical_assessment', verbose_name='Usuário')
    height = models.FloatField(verbose_name='Altura (cm)')
    weight = models.FloatField(verbose_name='Peso (kg)')
    date_of_birth = models.DateField(verbose_name='Data de Nascimento')
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')], verbose_name='Gênero')
    bf = models.FloatField(verbose_name='Percentual de Gordura Corporal')
    bcm = models.FloatField(verbose_name='Massa Corporal Magra')
    biceps_right = models.FloatField(verbose_name='Bíceps Direito (cm)')
    biceps_left = models.FloatField(verbose_name='Bíceps Esquerdo (cm)')
    anti_brachium_right = models.FloatField(verbose_name='Antebraço Direito (cm)')
    anti_brachium_left = models.FloatField(verbose_name='Antebraço Esquerdo (cm)')
    coxa_right = models.FloatField(verbose_name='Coxa Direita (cm)')
    coxa_left = models.FloatField(verbose_name='Coxa Esquerda (cm)')
    cintura = models.FloatField(verbose_name='Cintura (cm)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Avaliação Física'
        verbose_name_plural = 'Avaliações Físicas'

    def __str__(self):
        return f"Avaliação Física - {self.user.username}"
