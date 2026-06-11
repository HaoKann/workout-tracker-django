FROM python:3.12-slim

# Устанавливаем переменные окружения, чтобы Python не писал .pyc файлы и не буферизировал stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# Копируем проект
COPY . /app/