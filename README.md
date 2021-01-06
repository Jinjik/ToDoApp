# Тестовое задание от ReTech Labs

## [Тестовое задание](tz_ReTech.pdf)

## Руководство по запуску


### Установка:

Установить python v.3.9

```commandline
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### Панель администратора
Панель администратора расположена по адресу [/admin](http://127.0.0.1:8000/admin)

В админ панели создаются пользователи, работники (на основе пользователей) и организации.

### API
Авторизация: [/api/signin](http://127.0.0.1:8000/api/signin)

POST-запрос
```json
{
    "email": "", 
    "organization":"", 
    "password":""
}
```

Выход из системы: [/api/signout](http://127.0.0.1:8000/api/signout)

Получить список доступных ToDo заданий: [/api/tasks](http://127.0.0.1:8000/api/tasks)

#### Создание записи: 

[/api/tasks](http://127.0.0.1:8000/api/tasks/)

POST-запрос
```json
{
    "title": "",
    "description": "",
    "completed": false,
    "organization": null
}
```

##### Обновление записи: 

/api/tasks/(?P\<id\>\d+)/

PUT-запрос (Все параметры должны присутствовать)

```json
{
        "id": id: int,
        "title": "",
        "description": "",
        "completed": true/false,
        "organization": 
    },
```

##### Удаление записи:

/api/tasks/(?P\<id\>\d+)/

DELETE - запрос