from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import WorkOut, Exercise
from django.contrib.auth.models import User
from .forms import WorkOutForm
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class WorkOutList(ListView):
    # Указываем, с какой моделью (таблицей) работаем
    model = WorkOut
    # Указываем путь к нашему HTML-шаблону
    template_name = 'workouts/main.html'
    context_object_name = 'workouts'


class WorkOutCreate(CreateView):
    model = WorkOut
    form_class = WorkOutForm 
    template_name = 'workouts/workout_form.html'

    # Куда перенаправить после успешного сохранения
    success_url = reverse_lazy('workout_list')

    # Тот самый перехватчик конвейера
    def form_valid(self, form):
        # form.instance — это наша тренировка. Аналог commit=False
        form.instance.user = User.objects.first()

        # Создаем зеленое уведомление
        messages.success(self.request, 'Тренировка успешно добавлена! 🎉')
        
        # Возвращаем форму на конвейер для финального сохранения в базу
        return super().form_valid(form)