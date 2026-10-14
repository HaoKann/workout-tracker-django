from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import WorkOut, WorkOutSet, RoutineExercise, WorkOutRoutine, Exercise
from django.contrib.auth import get_user_model
from .forms import WorkOutForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch, Q
import json
from django.db import transaction
from django.http import JsonResponse
import logging
from django.core.cache import cache
from rest_framework import generics
from .serializers import ExerciseSerializer, RoutineSerializer, ExerciseListSerializer
from .forms import WorkoutSetFormSet

logger = logging.getLogger(__name__)

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
                Prefetch('sets', queryset=WorkOutSet.objects.filter(weight__gt=0).select_related('exercise'), to_attr='heavy_sets')
            )
        )
    
    def get_context_data(self, **kwargs):
        # Получаем стандартный набор данных
        context = super().get_context_data(**kwargs)
        
        # Делаем один быстрый запрос в базу: считаем все подходы этого пользователя
        context['total_sets'] = WorkOutSet.objects.filter(workout__user=self.request.user).count()
        
        return context

class WorkOutDetail(LoginRequiredMixin, DetailView):
    model=WorkOut
    template_name='workouts/workout_detail.html'

class WorkOutCreate(LoginRequiredMixin, CreateView):
    model = WorkOut
    form_class = WorkOutForm 
    template_name = 'workouts/workout_form.html'

    # Куда перенаправить после успешного сохранения
    success_url = reverse_lazy('workout_list')

    # Тот самый перехватчик конвейера
    def form_valid(self, form):
        # 1. Достаем пустой (или заполненный с ошибками) формсет
        context = self.get_context_data()
        formset = context['formset']
        
        # 2. Если в подходах всё заполнено верно:
        if formset.is_valid():
            # form.instance — это наша тренировка и привязываем её к юзеру
            form.instance.user = self.request.user
            
            # super().form_valid(form) физически создаст запись в БД
            # и сохранит новую тренировку внутри self.object
            response = super().form_valid(form)
            
            # 3. Привязываем подходы к свежесозданной тренировке
            formset.instance = self.object
            
            # 4. Сохраняем подходы
            formset.save()
            
            # Создаем зеленое уведомление
            messages.success(self.request, 'Тренировка успешно добавлена! ')
            
            return response
        else:
            # Если в формсете ошибка (например, вес буквами), 
            # возвращаем страницу обратно, чтобы показать эти ошибки
            return self.render_to_response(self.get_context_data(form=form))
        
        # Возвращаем форму на конвейер для финального сохранения в базу

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Если пользователь нажал "Сохранить", передаем введенные данные 
        if self.request.POST:
            context['formset'] = WorkoutSetFormSet(self.request.POST)
        else:
            context['formset'] = WorkoutSetFormSet()
            
        return context
        
        
    
class WorkOutUpdate(LoginRequiredMixin, UpdateView):
    model = WorkOut
    form_class = WorkOutForm
    template_name = 'workouts/workout_form.html'
    
    success_url = reverse_lazy('workout_list')
    
    def get_queryset(self):
        return WorkOut.objects.filter(user = self.request.user)
    
    def get_context_data(self, **kwargs):
        # 1. Получаем базовый словарь со всеми стандартными данными
        context = super().get_context_data(**kwargs)
    
        # 2. Создаем формсет, передаем ему текущую тренировку (self.object)
        # и сохраняем всё это в словарь под ключом 'formset'
        context['formset'] = WorkoutSetFormSet(instance=self.object)
        
        # 3. Возвращаем обновленный словарь
        return context
    
    def form_valid(self, form):
        # 1. Достаем наш формсет из контекста
        context = self.get_context_data()
        formset = context['formset']
        
        # 2. Проверка на ошибки в formset
        if formset.is_valid():
            # Сохраняем саму тренировку в базу данных
            self.object = form.save() 
            formset.instance = self.object
            # 3. Сохраняем подходы
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
            
    
class WorkOutDelete(LoginRequiredMixin, DeleteView):
    model = WorkOut
    success_url = reverse_lazy('workout_list')
    
    def get_queryset(self):
        return WorkOut.objects.filter(user = self.request.user)
    
    def form_valid(self, form):
        logger.warning("Тренировка успешно удалена!")
        return super().form_valid(form)
    
    
class RoutineList(LoginRequiredMixin, ListView):
    model = WorkOutRoutine
    template_name = 'workouts/routines.html'
    
    def get_queryset(self):
        # 1. Создаем уникальный ключ (например: "routines_user_5")
        cache_key = f"routines_user_{self.request.user.id}"
        
        # 2. Пытаемся достать данные
        routines = cache.get(cache_key)
        
        # 3. Если в кэше пусто (None)
        if not routines:
            routines = WorkOutRoutine.objects.filter(user = self.request.user)
            cache.set(cache_key, routines, 120)
        
        return routines
        
class RoutineCreate(LoginRequiredMixin, CreateView):
    model = WorkOutRoutine
    fields= ['title', 'notes']
    template_name = 'workouts/create_routine.html'
    success_url = reverse_lazy('workout_routines')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Рутина успешно создана!")
        
        return super().form_valid(form)


class RoutineDetail(LoginRequiredMixin, DetailView):
    model = WorkOutRoutine
    template_name = 'workouts/routine_details.html'
    
    # Метод для отлова POST-запросов
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        RoutineExercise.objects.create(routine=self.object, exercise_id=request.POST.get('exercise'))
        
        return redirect('routine_details', self.object.pk)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['exercises'] = Exercise.objects.all()
        
        return context
    
    def get_queryset(self):
            return WorkOutRoutine.objects.filter(user = self.request.user)


class RoutineExerciseDelete(LoginRequiredMixin,DeleteView):
    model = RoutineExercise
    
    
    def get_success_url(self):
        routine_id = self.object.routine.id
        return reverse('routine_details', kwargs={'pk': routine_id})
    
    def get_queryset(self):
        return RoutineExercise.objects.filter(routine__user = self.request.user)
    
    def form_valid(self, form):
        logger.warning("Упражнение было удалено из рутины!")
        return super().form_valid(form)
    
    

def update_exercise_order(request):
    data = json.loads(request.body)
    
    with transaction.atomic():
        for index, item_id in enumerate(data['order']):
            RoutineExercise.objects.filter(id=item_id).update(order=index)
            
    return JsonResponse({"status": "ok"})


class ExerciseListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    
    def get_queryset(self):
            return Exercise.objects.filter(Q(user = self.request.user) | Q (user=None))
    
    # Вклиниваемся в процесс сохранения
    def perform_create(self, serializer):
        # Сохраняем упражнение, принудительно добавляя текущего юзера и флаг is_custom
        serializer.save(user=self.request.user, is_custom=True)
    
    
class ExerciseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    
# 1. Дженерик для списка (GET) и создания (POST)
class RoutineListCreateAPI(generics.ListCreateAPIView):
    queryset = WorkOutRoutine.objects.all()
    serializer_class = RoutineSerializer
    
# 2. Дженерик для просмотра одной рутины, обновления и удаления (GET, PUT, DELETE)
class RoutineDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkOutRoutine.objects.all()
    serializer_class = RoutineSerializer
    
    
class ExerciseListAPI(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseListSerializer
    
    def perform_create(self, serializer):
        # Принудительно ставим текущего пользователя и флаг кастомного упражнения
        serializer.save(user=self.request.user, is_custom=True)
        
        
class ExerciseList(LoginRequiredMixin, ListView):
    model = Exercise
    template_name='exercise_list.html'
    
    def get_queryset(self):
        return Exercise.objects.filter(Q(user = self.request.user) | Q (user=None))
        