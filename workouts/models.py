from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WorkOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=100, help_text="Название тренировки (например, 'День ног')")
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True, help_text="Заметки к тренировке")
    photo = models.ImageField(upload_to='workout_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.date} ({self.user.username})"
    
# Справочник упражнений
class Exercise(models.Model):
    name = models.CharField(max_length=100, help_text='Например: Жим лежа')
    description = models.TextField(blank=True, null=True, help_text='Техника выполнения или мышечная группа')

    def __str__(self):
        return self.name
    

# Конкретный подход
class WorkoutSet(models.Model):
    # Привязываем подход к конкретной тренировке
    workout = models.ForeignKey(WorkOut, on_delete=models.CASCADE, related_name='sets')
    # Привязываем подход к конкретному упражнению из справочника
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    weight = models.DecimalField(max_digits=5, decimal_places=1, help_text='Вес в кг')
    reps = models.IntegerField(help_text='Количество повторений')

    def __str__(self):
        return f"{self.exercise.name}: {self.weight} кг x {self.reps}"