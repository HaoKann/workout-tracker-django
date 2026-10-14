from django.contrib import admin
from .models import WorkOut, Exercise, WorkOutSet, WorkOutExercise
# Register your models here.


# Регистрируем справочник упражнений
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Создаем "встроенную" панель для подходов
class WorkOutSetInline(admin.TabularInline):
    model = WorkOutSet
    extra = 1 # Сколько пустых строк для подходов показывать по умолчанию


class WorkOutExerciseInline(admin.TabularInline):
    model = WorkOutExercise
    extra = 1

# Обновляем старую админку для тренировок
@admin.register(WorkOut)
class WorkOutAdmin(admin.ModelAdmin):
    # Эти поля будут отображаться в виде красивой таблицы
    list_display = ('title', 'user', 'date')
    # Добавляем фильтрацию по дате и пользователю
    list_filter = ('date', 'user')
    # Добавляем поиск по названию
    search_fields = ('title',)
    inlines = [WorkOutExerciseInline]


# Регистрируем подходы как отдельную таблицу
@admin.register(WorkOutSet)
class WorkOutSetAdmin(admin.ModelAdmin):
    list_display = ('workout_exercise', 'weight', 'reps')
    list_filter = ('workout_exercise',)