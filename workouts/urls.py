from django.urls import path
from . import views

urlpatterns = [
    # Путь пустой '', значит он будет срабатывать на главной странице приложения
    # Заменяем функцию на вызов метода as_view() у нашего класса
    path('', views.WorkOutList.as_view(), name='workout_list'),
    path('new/', views.WorkOutCreate.as_view(), name='workout_create'),
    path('update/<int:pk>/', views.WorkOutUpdate.as_view(), name='workout_update'),
    path('delete/<int:pk>/', views.WorkOutDelete.as_view(), name='workout_delete'),
]