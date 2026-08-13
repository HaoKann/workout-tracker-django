from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile
# Register your models here.

# Склеивание профиля пользователя и основной информации пользователя для удобства редактирования
class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    inlines = [UserProfileInline]
    
admin.site.register(CustomUser, CustomUserAdmin)