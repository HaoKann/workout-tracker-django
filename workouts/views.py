from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkOut
# Create your views here.

def workout_list(request):
    # Достаем все записи из базы данных с помощью ORM
    workouts = WorkOut.objects.all()

    # Формируем простой текст для вывода
    result = "<br>".join([f"Тренировка: {w.title} | Дата: {w.date}" for w in workouts])

    return HttpResponse(f"<h1>Мой Workout Tracker</h1><p>{result}</p>")
