# Roadmap: Изучение Django с нуля до Middle

## 🟦 Блок 1: Фундамент (The Django Way)
- [x] Настройка окружения (Docker, PostgreSQL, Django)
- [x] Понимание архитектуры MTV (Model-Template-View)
- [x] Основы ORM: Модели и Поля
- [x] Система миграций
- [x] URL Dispatcher и именование путей

➕ Дополнительно (обязательно для базы)
- [x] Структура проекта (apps, разделение логики)
- [x] Работа с settings.py (dev/prod конфиги)
- [x] Переменные окружения (.env)
- [x] Static и Media файлы (статика и загрузка файлов)

---

## 🟩 Блок 2: Логика и Отображение
- [x] Function Based Views (FBV)
- [x] Class Based Views (CBV): Базовые классы (ListView, DetailView, CreateView)
- [x] Django Templating Language (DTL): Наследование и фильтры
- [x] Работа с формами (Forms & ModelForms)
- [x] Кастомизация Django Admin

➕ Дополнительно
- [x] Django Messages Framework
- [x] Работа с загрузкой файлов (FileField, ImageField)
- [x] Валидация форм (clean, validators)

---

## 🟧 Блок 3: Продвинутый Backend
- [ ] Custom User Model (Абстрактный пользователь)
- [ ] Оптимизация запросов: select_related и prefetch_related
- [ ] Middleware (Свои прослойки)
- [ ] Django Signals
- [ ] Аутентификация и права доступа (Permissions)

➕ Дополнительно (очень важно)
- [ ] Транзакции (atomic)
- [ ] Обработка ошибок (custom exceptions, handlers)
- [ ] Логирование (logging)
- [ ] Работа с кэшем (Django cache + Redis)
- [ ] Основы безопасности (CSRF, XSS, CORS)

---

## 🟪 Блок 4: API и Экосистема (DRF)
- [ ] Django REST Framework: Serializers
- [ ] APIView, ViewSets и Routers
- [ ] JWT Аутентификация
- [ ] Celery + Redis: Фоновые задачи
- [ ] Тестирование (Unit tests / Pytest)

➕ Дополнительно (Middle уровень)
- [ ] Pagination
- [ ] Фильтрация (django-filter)
- [ ] Throttling (ограничение запросов)
- [ ] Permissions в DRF
- [ ] Версионирование API

---

## 🟥 Блок 5: Архитектура и Практика (ключ к Middle)
- [ ] Разделение на слои (services / repositories) — *с учетом специфики "The Django Way"*
- [ ] Чистая архитектура в Django-проекте
- [ ] Повторное использование кода (DRY)
- [ ] Работа с бизнес-логикой вне views (Service Layer)

---

## 🟫 Блок 6: Деплой и Production (обязательно)
- [ ] Подготовка к продакшену (DEBUG=False)
- [ ] Gunicorn / Uvicorn
- [ ] Nginx
- [ ] Docker Compose (production)
- [ ] Настройка PostgreSQL в проде
- [ ] Хостинг (VPS / Cloud)
- [ ] Сбор статики (collectstatic)