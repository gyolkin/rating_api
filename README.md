# Простой блог на Django
[![Version_of_Python](https://img.shields.io/badge/python-3.7-orange?style=flat&logo=python&logoColor=white)](#)
[![Version_of_Django](https://img.shields.io/badge/django-3.2-green?style=flat&logo=django&logoColor=white)](#)
[![Docker_Compose](https://img.shields.io/badge/docker-compose-blue?style=flat&logo=docker&logoColor=white)](#)
[![Github Actions](https://img.shields.io/badge/github-actions-brightgreen?style=flat&logo=github&logoColor=white)](https://github.com/gyolkin/yamdb)

## Описание
«YaMDB» — это API, построенное на Django Rest Framework. Пользователям, в зависимости от выданных прав, доступны возможности просмотра, создания и редактирования жанров, категорий (музыка, фильмы), самих произведений и отзывов к ним. Отзывы могут быть прокомментированы каждым пользователем. Оценка пользователя может варьироваться от 1 до 10, при получении произведения будет отображаться общая (средняя) оценка.

## Регистрация
В процессе получения токена авторизации необходимо сделать POST-запрос, предоставив почтовый код подтверждения вида *bn06q5-d96eb8465ae46930926086160d053c13*. Поскольку «боевой» почтовый сервер не настроен, все письма появляются локально в папке *sent_emails* в корне проекта. Письмо с кодом подтверждения во время тестирования проекта следует искать именно там.

## Технологический стек
- Python
- Django
- Django Rest Framework
- Docker
- PostgreSQL
- nginx
- Github Actions

## Зависимости
Файл с зависимостями requirements.txt находится в папке *api_yamdb*.

## Запуск на локальном компьютере
Помимо стандартного запуска Django-проекта предусмотрена возможность запуска проекта в Docker (с docker-compose). Для этого необходимо создать в папке *infra* файл .env и заполнить его данными по примеру файла .env.example. Далее, находясь в папке *infra*, требуется выполнить команду:
```
docker-compose up -d
```
Проект будет собран в «тихом режиме», после чего необходимо последовательно выполнить команды: 
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic
```
Можно также сразу создать администратора с помощью команды:
```
docker-compose exec web python manage.py createsuperuser
```
При успешном запуске проект и администраторская панель станут доступны здесь:
```
http://localhost
http://localhost/admin
```
Документация к API:
```
http://localhost/redoc
```

## Github Actions
Для демонтрации навыков CI/CD разработки используется сервис Github Actions. Интегрирована следующая функциональность: проверка кодовой базы проекта на соответствие правилам pep8, сборка и пуш docker-образа в DockerHub, деплой и запуск проекта на сервере, отправка сообщения в Telegram при успешном завершении процесса. Workflow-файл располагается в папке *.github/workflows*.