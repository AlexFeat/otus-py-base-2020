FROM python:3.9-buster

# объявляем рабочую директорию
WORKDIR /var/app

# устанавливаем зависимости проекта
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY foodcourt/pyproject.toml foodcourt/poetry.lock ./
RUN poetry install --no-interaction --no-ansi

# копирование кода проекта в докер
COPY foodcourt/foodcourt .

#регламентируем порт
EXPOSE 5000
