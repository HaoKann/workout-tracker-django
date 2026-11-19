from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, CustomUserCreationForm, ProfileUpdateForm
from .models import UserProfile
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm 
from workouts.models import WorkOut, WorkOutSet

def register_view(request):
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
        
       
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Получаем пользователя и логиним его
            user = form.get_user()
            auth_login(request, user)
            return redirect('workout_list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})     

 
@login_required
def profile(request): 
    # Проверяем, передан ли GET-параметр ?edit=y
    edit_mode = request.GET.get('edit') == 'y'
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile')
    else:
        # Если это обычный GET-запрос, просто заполняем форму текущими данными пользователя
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=user_profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'edit_mode': edit_mode,
        'total_workouts': WorkOut.objects.filter(user=request.user).count(),
        'total_sets': WorkOutSet.objects.filter(workout_exercise__workout__user=request.user).count(),
    }   
    return render(request, 'users/profile.html', context)