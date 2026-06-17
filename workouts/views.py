from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import WorkOut
from django.contrib.auth.models import User
from .forms import WorkOutForm
from django.contrib import messages
# Create your views here.

def workout_list(request):
    # Достаем все записи из базы данных с помощью ORM
    workouts = WorkOut.objects.all()

    # Передаем данные в шаблон через словарь контекста
    context = {
        'workouts': workouts
    }

    # render сам ищет папку templates внутри зарегистрированных приложений
    return render(request, 'workouts/main.html', context)


def workout_create(request):
    # Если пользователь отправил заполненную форму
    if request.method == 'POST':
        form = WorkOutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)

            # ХАК: Так как мы еще не делали систему логина, 
            # жестко привязываем тренировку к первому пользователю в базе (к тебе)
            workout.user = User.objects.first()

            workout.save()
            messages.success(request, 'Тренировка успешно добавлена! 🎉')
            return redirect('workout_list')
    else:
        # Если пользователь просто открыл страницу, показываем пустую форму
        form = WorkOutForm()

    return render(request, 'workouts/workout_form.html', {'form':form})
