from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'weight']
        labels = {
            'avatar': 'Аватар профиля',
            'weight': 'Текущий вес (кг)',
        }
        widgets = {
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'style': 'background-color: #2d3748; color: white; border: 1px solid #4a5568; padding: 8px; border-radius: 5px;'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control-file',
                'style': 'color: #cbd5e0'
            })
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