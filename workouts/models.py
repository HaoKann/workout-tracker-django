from django.db import models
from django.conf import settings

# Create your models here.
class WorkOut(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='workouts'
    )
    title = models.CharField(max_length=100, help_text="Название тренировки (например, 'День ног')")
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True, help_text="Заметки к тренировке")
    photo = models.ImageField(upload_to='workout_images/', blank=True, null=True)
    
    exercises = models.ManyToManyField('Exercise', related_name='workouts')

    

    def __str__(self):
        return f"{self.title} - {self.date} ({self.user.username})"
    
# Справочник упражнений
class Exercise(models.Model):
    name = models.CharField(max_length=100, help_text='Например: Жим лежа')
    description = models.TextField(blank=True, null=True, help_text='Техника выполнения или мышечная группа')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='custom_exercises',
        null=True,
        blank=True
    )
    is_custom = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

# Упражнения в тренировке 
class WorkOutExercise(models.Model):
    workout = models.ForeignKey(WorkOut, on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.workout.title} - {self.exercise.name}"

# Конкретный подход
class WorkOutSet(models.Model):
    weight = models.DecimalField(max_digits=5, decimal_places=1, help_text='Вес в кг')
    reps = models.IntegerField(help_text='Количество повторений')
    workout_exercise = models.ForeignKey(WorkOutExercise, on_delete=models.CASCADE, related_name='sets', null=True)
    
    def __str__(self):
        return f"{self.workout_exercise.exercise.name}: {self.weight} кг x {self.reps}"
    
    
class WorkOutRoutine(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='routines'
    )
    title = models.CharField(max_length=100, help_text='Название рутины')
    notes = models.TextField(blank=True, null=True, help_text='Заметки')
    
    def __str__(self):
        return f"Рутина {self.title} пользователя {self.user.username}"
    

class RoutineExercise(models.Model):
    routine = models.ForeignKey(WorkOutRoutine, on_delete=models.CASCADE, related_name='routine_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    # Поле для сортировки, чтобы упражнения шли в правильном порядке
    order = models.PositiveIntegerField(default=0, help_text='Порядок упражнения в рутине')
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return f"{self.exercise.name} в {self.routine.title}"