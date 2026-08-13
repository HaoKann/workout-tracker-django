from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
    
    
class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")
    weight = models.FloatField(null=True, blank=True, verbose_name='Вес (кг)')
    
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='profile')