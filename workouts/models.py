from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WorkOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=100, help_text="Название тренировки (например, 'День ног')")
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True, help_text="Заметки к тренировке")

    def __str__(self):
        return f"{self.title} - {self.date} ({self.user.username})"