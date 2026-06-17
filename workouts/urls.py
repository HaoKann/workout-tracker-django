from django.urls import path
from . import views

urlpatterns = [
    # Путь пустой '', значит он будет срабатывать на главной странице приложения
    path('', views.workout_list, name='workout_list'),
    path('/new/', views.workout_create, name='workout_create')
]