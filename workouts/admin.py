from django.contrib import admin
from .models import WorkOut
# Register your models here.

@admin.register(WorkOut)
class WorkOutAdmin(admin.ModelAdmin):
    # Эти поля будут отображаться в виде красивой таблицы
    list_display = ('title', 'user', 'date')
    # Добавляем фильтрацию по дате и пользователю
    list_filter = ('date', 'user')
    # Добавляем поиск по названию
    search_fields = ('title',)