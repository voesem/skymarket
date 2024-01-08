Данная работа представляет собой backend-часть для сайта объявлений.
В бэкенд-части проекта реализован следующий функционал:
* Авторизация и аутентификация пользователей.
* Распределение ролей между пользователями (пользователь и админ).
* CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
* Под каждым объявлением пользователи могут оставлять отзывы.

На первом этапе осуществлена общая настройка проекта:
1. Подключена база данных Postgres.
2. Подключен CORS headers.
3. Подключен Swagger.

На втором этапе создана модель пользователя, а также настроена авторизация и аутентификация пользователей 
по ролям (админ и обычный пользователь) с использованием библиотек djoser и simple_jwt.

На третьем этапе созданы модели объявлений и отзывов.

На четвертом этапе созданы контроллеры для работы с объявлениями и отзывами к ним.

На пятом этапе определены права доступа:
**Анонимный пользователь может**:

получать список объявлений.

**Пользователь может:**

- получать список объявлений,
- получать одно объявление,
- создавать объявление
- редактировать и удалять свое объявление,
- получать список комментариев,
- создавать комментарии,
- редактировать/удалять свои комментарии.

**Администратор может:**

дополнительно к правам пользователя редактировать или удалять
объявления и комментарии любых других пользователей.

Проект можно запустить следующим образом:
1. Склонировать репозиторий.
2. Установить виртуальное окружение venv.
3. Установить зависимости командой pip install -r requirements.txt
4. Находясь в директории app, запустить приложение командой python manage.py runserver