from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkOut
# Create your views here.

def workout_list(request):
    # Достаем все записи из базы данных с помощью ORM
    workouts = WorkOut.objects.all()

    # Передаем данные в шаблон через словарь контекста
    context = {
        'workouts': workouts
    }

    # render сам ищет папку templates внутри зарегистрированных приложений
    return render(request, 'workouts/index.html', context)
