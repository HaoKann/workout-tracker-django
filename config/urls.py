from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем все пути из нашего приложения workouts на главную страницу
    path('', include('workouts.urls'), name='home'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register_view, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'), 
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('__debug__/', include("debug_toolbar.urls"))
]


# Добавляем раздачу медиа-файлов во время разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)