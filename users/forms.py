from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['weight', 'avatar']
        labels = {
            'weight': 'Текущий вес (кг)',
            'avatar': 'Аватарка',
        }
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Например, 72.5'}),
            'avatar': forms.FileInput(attrs={'accept': 'image/*'}),
        }





# Форма регистрации 
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        
        model = CustomUser
        # Указываем поля при регистрации
        fields = ('username', 'email')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''
            # Добавляем стили в духе твоего темного дизайна
            field.widget.attrs['class'] = 'wf-input'