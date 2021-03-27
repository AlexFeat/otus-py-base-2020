FROM python:3.9-buster

# объявляем рабочую директорию
WORKDIR /var/app

# устанавливаем зависимости проекта
COPY foodcourt/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# копирование кода проекта в докер
COPY foodcourt .

#регламентируем порт
EXPOSE 5000

# запускаем приложение
CMD ./app.py