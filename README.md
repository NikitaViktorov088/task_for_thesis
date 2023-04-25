# Тестовое задание для компании Thesis
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


Задание
Тестовое задание Python/Django/DRF

По результатам тестового задания мы должны оценить уровень знания ключевых возможностей языка и перечисленных фреймворков.
Описание задачи
Разработать API для представления структуры компании:
Список департаментов
Список сотрудников (как общий, так и по департаментам отдельно)
Модель данных:

Сотрудник содержит атрибуты:
ФИО
Фото
Должность
Оклад
Возраст
Департамент

Департамент содержит:
Название
Связь с сотрудником - директором департамента

Должна быть обеспечена уникальности связки “сотрудник-департамент”.
Должен быть оптимизирован запрос поиска по фамилии сотрудника.
Админка

Должна быть реализована админка, в которой можно посмотреть на данные модели и их модифицировать.

REST API
API для получения списка сотрудников + реализовать фильтр для поиска по фамилии и по id департамента
Добавление/удаление сотрудников через API
API для получения списка департаментов (включает искусственное поле с числом сотрудников + поле с суммарным окладам по всем сотрудникам)
API со списком сотрудников - с пагинацией, API со списком департаментов - без пагинации
Доступ к списку сотрудников - только для авторизованных пользователей, доступ к списку департаментов - доступен и для анонимных пользователей
Ожидаемый результат
Набор API методов для работы с данными по сотрудникам и департаментам
Swagger документация по API методам
Админка по модели данных

## Запуск проекта
1. Склонируйте репозиторий на локальную машину.

    ```
    git clone https://github.com/NikitaViktorov088/task_for_thesis.git
    ```

2. Установите и активируйте виртуальное окружение

    ```
    python3 -m venv venv
    ```

3. Активируйте виртуальное окружение:

    ```
    source venv/bin/activate
    ```

4. Установите зависимости из файла requirements.txt:

    ```  
    pip install -r requirements.txt  
    ```

5. Создайте .env файл в директории backend/foodgram/, в котором должны содержаться следующие переменные для подключения к базе PostgreSQL:

    ```
    SECRET_KEY=django-insecure--sb+o^x06mw7d$0w5j3fy@3%+d@y@-+k6xt4*+g8exs=mhc+^2
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    ```

6. В директории проекта выполните команду для создания и запуска контейнеров:
    ```
    docker compose up
    ```

7. В контейнере web выполните миграции, соберите статику, создайте суперпользователя и загрузите данные для бд из json:
    ```
    docker compose exec backend python manage.py migrate
    docker compose exec backend python manage.py collectstatic
    docker compose exec backend python manage.py loaddata dump.json
    docker compose exec backend python manage.py createsuperuser
    ```
8. Документация swagger/redoc доступны по адресам:
    ```
    http://localhost/swagger/
    http://localhost/redoc/
    ```

9. Админка доступна по адресу:
    ```
    http://localhost/admin/
    ```

  ## Автор  
  
  [Викторов Никита](https://github.com/NikitaViktorov088)
