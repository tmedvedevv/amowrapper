# Используем официальный образ Python на базе Alpine
FROM python:3.13-alpine

# Устанавливаем зависимости для Poetry
RUN apk add --no-cache \
    gcc \
    libffi-dev \
    musl-dev \
    && pip install --upgrade pip \
    && pip install poetry \
    && apk del gcc libffi-dev musl-dev

# Устанавливаем рабочую директорию
WORKDIR /

# Копируем файл зависимостей в контейнер
COPY pyproject.toml /amowrapper/

COPY . /app/