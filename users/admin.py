from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Добавление новых полей к стандартным блокам админки
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('avatar', 'weight')}), # <-- ВОТ ЭТА ЗАПЯТАЯ!
    )
admin.site.register(CustomUser, CustomUserAdmin)