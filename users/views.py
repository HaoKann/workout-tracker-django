from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, CustomUserCreationForm



def register(request):
    # Если кто-то нажал кнопку "Зарегистрироваться" (отправил данные)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Создаем пользователя в базе данных PostgreSQL
            username = form.cleaned_data.get('username')
            messages.success(request, f"Аккаунт {username} успешно создан!")
            return redirect('login')
    else:
        # Если человек просто перешел на страницу регистрации, выдаем пустую форму
        form = CustomUserCreationForm()      

    return render(request, 'users/register.html', {'form': form})
        
        
@login_required
def profile(request): 
    # Проверяем, передан ли GET-параметр ?edit=y
    edit_mode = request.GET.get('edit') == 'y'

    if request.method == "POST":
        # Передаем POST-данные и файлы (request.FILES), а также указываем instance (кого именно редактируем)
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile')
    else:
        # Если это обычный GET-запрос, просто заполняем форму текущими данными пользователя
        form = UserUpdateForm(instance=request.user)
        
    context = {
        'form': form,
        'edit_mode': edit_mode
    }   
    return render(request, 'users/profile.html', context)
