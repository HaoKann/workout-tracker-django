from django import forms
from django.contrib.auth import get_user_model

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