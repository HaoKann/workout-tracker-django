from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import WorkOut, Exercise, WorkoutSet
from django.contrib.auth import get_user_model
from .forms import WorkOutForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch

User = get_user_model()

class WorkOutList(LoginRequiredMixin, ListView):
    # Указываем, с какой моделью (таблицей) работаем
    model = WorkOut
    # Указываем путь к нашему HTML-шаблону
    template_name = 'workouts/main.html'
    context_object_name = 'workouts'
    
    def get_queryset(self):
        return (
            WorkOut.objects.filter(user = self.request.user)
            .select_related('user')
            .prefetch_related(
                Prefetch('sets', queryset=WorkoutSet.objects.filter(weight__gt=0).select_related('exercise'), to_attr='heavy_sets')
            )
        )
    
    def get_context_data(self, **kwargs):
        # Получаем стандартный набор данных
        context = super().get_context_data(**kwargs)
        
        # Делаем один быстрый запрос в базу: считаем все подходы этого пользователя
        context['total_sets'] = WorkoutSet.objects.filter(workout__user=self.request.user).count()
        
        return context


class WorkOutCreate(LoginRequiredMixin, CreateView):
    model = WorkOut
    form_class = WorkOutForm 
    template_name = 'workouts/workout_form.html'

    # Куда перенаправить после успешного сохранения
    success_url = reverse_lazy('workout_list')

    # Тот самый перехватчик конвейера
    def form_valid(self, form):
        # form.instance — это наша тренировка. Аналог commit=False
        form.instance.user = self.request.user

        # Создаем зеленое уведомление
        messages.success(self.request, 'Тренировка успешно добавлена! 🎉')
        
        # Возвращаем форму на конвейер для финального сохранения в базу
        return super().form_valid(form)

    
class WorkOutUpdate(LoginRequiredMixin, UpdateView):
    model = WorkOut
    form_class = WorkOutForm
    template_name = 'workouts/workout_form.html'
    
    success_url = reverse_lazy('workout_list')
    
    def get_queryset(self):
        return WorkOut.objects.filter(user = self.request.user)
    
class WorkOutDelete(LoginRequiredMixin, DeleteView):
    model = WorkOut
    success_url = reverse_lazy('workout_list')
    
    def get_queryset(self):
        return WorkOut.objects.filter(user = self.request.user)
    