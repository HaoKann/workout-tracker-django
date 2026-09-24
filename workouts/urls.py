from django.urls import path
from . import views

urlpatterns = [
    # Путь пустой '', значит он будет срабатывать на главной странице приложения
    # Заменяем функцию на вызов метода as_view() у нашего класса
    path('', views.WorkOutList.as_view(), name='workout_list'),
    path('new/', views.WorkOutCreate.as_view(), name='workout_create'),
    path('update/<int:pk>/', views.WorkOutUpdate.as_view(), name='workout_update'),
    path('delete/<int:pk>/', views.WorkOutDelete.as_view(), name='workout_delete'),
    path('routines/', views.RoutineList.as_view(), name='workout_routines'),
    path('routines/create/', views.RoutineCreate.as_view(), name='create_routine'),
    path('routines/details/<int:pk>/', views.RoutineDetail.as_view(), name='routine_details'),
    path('routines/delete/<int:pk>/', views.RoutineExerciseDelete.as_view(), name='routine_delete_exercise'),
    path('routines/change_order/', views.update_exercise_order, name='update_exercise_order'),
    path('api/create/exercises/', views.ExerciseListCreateAPI.as_view(), name='exercises'),
    path('api/exercises/<int:pk>/', views.ExerciseDetailAPI.as_view(), name='exercise_detail'),
    path('api/routines/', views.RoutineListCreateAPI.as_view(), name='routine_list'),
    path('api/routines/<int:pk>/', views.RoutineDetailAPI.as_view(), name='routine_detail'),
    path('api/exercises/',views.ExerciseListAPI.as_view(), name='exercise_list')
]
