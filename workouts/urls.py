from django.urls import path
from . import views

urlpatterns = [
    # Путь пустой '', значит он будет срабатывать на главной странице приложения
    # Заменяем функцию на вызов метода as_view() у нашего класса
    path('', views.WorkOutList.as_view(), name='workout_list'),
    path('new/', views.WorkOutCreate.as_view(), name='workout_create')
]