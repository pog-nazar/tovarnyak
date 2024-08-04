# Используем базовый образ с Python 3.11
FROM python:3.11-slim

# Установите рабочую директорию
WORKDIR /tovarnyak

# Копируйте файл зависимостей
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте остальные файлы
COPY . .

# Укажите команду для запуска приложения
CMD ["python", "bot/bot.py"]
