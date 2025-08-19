from django.contrib import admin
from .models import Profile, PhysicalAssessment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture', 'nivel', 'created_at')
    search_fields = ('user__username', 'nivel')

@admin.register(PhysicalAssessment)
class PhysicalAssessmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'date_of_birth', 'gender', 'bf', 'bcm', 'biceps_right', 'biceps_left', 'anti_brachium_right', 'anti_brachium_left', 'coxa_right', 'coxa_left', 'cintura')
    search_fields = ('user__username', 'gender')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    


