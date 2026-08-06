from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile
from workouts.models import WorkOut

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_user_profile = UserProfile(user=instance)
        
        new_user_profile.save()
        
@receiver(post_save, sender=CustomUser)
def create_basic_workout(sender, instance, created, **kwargs):
    if created:
        new_basic_workout = WorkOut(user=instance, title='Новая базовая тренировка')
        
        new_basic_workout.save()