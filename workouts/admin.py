from django.contrib import admin
from .models import WorkOut, Exercise, WorkoutSet
# Register your models here.


# Регистрируем справочник упражнений
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Создаем "встроенную" панель для подходов
class WorkOutSetInline(admin.TabularInline):
    model = WorkoutSet
    extra = 1 # Сколько пустых строк для подходов показывать по умолчанию


# Обновляем  старую админку для тренировок
@admin.register(WorkOut)
class WorkOutAdmin(admin.ModelAdmin):
    # Эти поля будут отображаться в виде красивой таблицы
    list_display = ('title', 'user', 'date')
    # Добавляем фильтрацию по дате и пользователю
    list_filter = ('date', 'user')
    # Добавляем поиск по названию
    search_fields = ('title',)
    inlines = [WorkOutSetInline]


# Регистрируем подходы как отдельную таблицу
@admin.register(WorkoutSet)
class WorkOutSetAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'weight', 'reps')
    list_filter = ('exercise',)