from django import forms
from .models import WorkOut
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator


class WorkOutForm(forms.ModelForm):
    # Явно описываем поле, чтобы повесить на него валидатор
    notes = forms.CharField(
        widget=forms.Textarea,
        validators=[MaxLengthValidator(500, 'Слишком длинное описание')],
    )

    class Meta:
        model = WorkOut
        fields = ['title', 'notes', 'photo']

    def clean_title(self):
        # 1. Достаем очищенный текст, который ввел пользователь
        title = self.cleaned_data.get('title')

        # 2. ПРОВЕРКА: Если длина названия меньше 3 символов
        if len(title) < 3:
            raise ValidationError('Название слишком короткое. Введите хотя бы 3 символа.')

        # 3. Если всё ок, возвращаем данные
        return title


        