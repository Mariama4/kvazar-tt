# kvazar-tt

## Описание

Данный проект является заключительной частью тестового задания для Квазар.
Суть задания является соединить воедино предыдущие модули:
- [API](https://github.com/Mariama4/kvazar-tt/tree/api)
- [UTILS](https://github.com/Mariama4/kvazar-tt/tree/utils)
- [ML](https://github.com/Mariama4/kvazar-tt/tree/ml)

А так-же добавление:
* Документации к API
* Документации к Проекту

**API реализовано на:**
* Python 3.11
* SQLite

**С использованием следующих библиотек:**
* Flask-SQLAlchemy 3.0.x
* python-dotenv
* flask-swagger-ui

**TODO:**

* Добавить слой Repository к Users (И рефакторинг остальных слоев, чтобы структура была верной)
* Улучшить качество docstring, type hinting

**Документация к API выполнена на swagger по стандарту openapi 3.0.0**

## Запуск проекта

Чтобы запустить проект, необходимо:

1. Скачать его:

```shell
git clone --branch=master https://github.com/Mariama4/kvazar-tt.git
```

2. Перейти в папку проекта:

```shell
cd kvazar-tt
```

3. Установить зависимости:

```shell
pip install -r requirements.txt
```

4. Запустить проект:

```shell
python app.py
```

# Использование API:

Если вы установили и запустили проект, то более подробную документацию можно увидеть тут [http://127.0.0.1:5000/api/docs/](http://127.0.0.1:5000/api/docs/)

## API App

> Version 1.0.0

API с модулем Users, который поддерживает CRUD и позволяет получить следующую информацию:
- Используя данные из таблицы User, подсчитывать количество пользователей, зарегистрированных за последние 7 дней;
- Получить топ 5 пользователей с самыми длинными именами;
- Получить процент пользователей, которые имеют адрес электронной почты, зарегистрированный в определенном домене (например, "example.com").

## Path Table

| Method | Path | Description |
| --- | --- | --- |
| GET | [/api/users/](#getapiusers) | Получение всех пользователей |
| GET | [/api/users](#getapiusers) | Получение пользователей с пагинацией |
| POST | [/api/users](#postapiusers) | Создание пользователя |
| GET | [/api/users/{id}](#getapiusersid) | Получение польльзователя по id |
| PATCH | [/api/users/{id}](#patchapiusersid) | Обновление пользователя по id |
| DELETE | [/api/users/{id}](#deleteapiusersid) | Удаление пользователя по id |
| POST | [/api/users/info](#postapiusersinfo) | Получение информации о пользователях |

## Reference Table

| Name | Path | Description |
| --- | --- | --- |
| User | [#/components/schemas/User](#componentsschemasuser) |  |

## Path Details

***

### [GET] /api/users/

- Summary  
Получение всех пользователей

#### Responses

- 200 Список пользователей

`application/json`

```json
[
  {
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
  },
  {
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
  }
]
```

- 403 Ошибка на стороне сервера

***

### [GET] /api/users

- Summary  
Получение пользователей с пагинацией

#### Parameters(Query)

```ts
page: integer
```

```ts
per_page: integer
```

#### Responses

- 200 Список пользователей

`application/json`

```json
[
  {
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
  },
  {
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
  }
]
```

- 403 Ошибка на стороне сервера

***

### [POST] /api/users

- Summary  
Создание пользователя

#### RequestBody

- application/json

```json
{
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
}
```

#### Responses

- 200 Пользователь создан

`application/json`

```json
{
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
}
```

- 403 Ошибка на стороне сервера

***

### [GET] /api/users/{id}

- Summary  
Получение пользователя по id

#### Responses

- 200 Пользователь получен

`application/json`

```json
{
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
}
```

- 403 Ошибка на стороне сервера

***

### [PATCH] /api/users/{id}

- Summary  
Обновление пользователя по id

#### RequestBody

- application/json

```json
{
    "email": string,
    "username": string
}
```

#### Responses

- 200 Пользователь получен

`application/json`

```json
{
    "email": string,
    "id": integer,
    "registration_date": datetime,
    "username": string
}
```

- 403 Ошибка на стороне сервера

***

### [DELETE] /api/users/{id}

- Summary  
Удаление пользователя по id

#### Responses

- 200 Пользователь удален

`application/json`

```json
{
  "deleted": boolean
}
```

- 403 Ошибка на стороне сервера

***

### [POST] /api/users/info

- Summary  
Получение информации о пользователях

- Description  
- Пользователи, которые зарегистрировались за последние 7 дней  
- Топ 5 пользователей, которые имеют самые длинные имена (по убыванию)  
- Процент пользователей, которые имеют адрес электронной почты, зарегистрированный в определенном домене (например, "example.com").

#### RequestBody

- application/json

```json
{
  "domain": string
}
```

#### Responses

- 200 Информация получена

`application/json`

```json
{
	"countUsersForWeek": integer,
	"percentOfDomain": {
		"domain": string,
		"percent": number
	},
	"topUsersWithLongestUsernames": [
		{
            "email": string,
            "id": integer,
            "registration_date": datetime,
            "username": string
        },
		{
            "email": string,
            "id": integer,
            "registration_date": datetime,
            "username": string
        }
	]
}
```

- 403 Ошибка на стороне сервера

## References

### #/components/schemas/User

```json
"id": integer
"username": string
"email": string
"registration_date": string
```
