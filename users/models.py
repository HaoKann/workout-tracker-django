from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")
    weight = models.FloatField(null=True, blank=True, verbose_name='Вес (кг)')

    def __str__(self):
        return self.username