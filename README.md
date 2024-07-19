# Проект test_ZHK

## Описание

Этот проект представляет собой веб-приложение на Django, для решения тестового задания.

## Установка

1. Клонируйте репозиторий:
2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv env
source env/bin/activate  # Для Windows используйте `env\Scripts\activate`
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Настройте переменные окружения. Создайте файл .env в корневом каталоге проекта и добавьте следующие переменные:
```
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=

```
5. Примените миграции и создайте суперпользователя:
```
python manage.py migrate
python manage.py createsuperuser
```
6. Запустите сервер:
```
python manage.py runserver
```
Структура проекта
apartments: Приложение для управления квартирами.\
buildings: Приложение для управления зданиями.\
users: Приложение для управления пользователями.\
water_meters: Приложение для управления счетчиками воды. Также хранит информацию о текущих тарифах\
