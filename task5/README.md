# Task5 overview

## Run
* python main.py

## Структура базы данных
|Column| Type                |Decription|
|-------|--------------------|----------|
|id     |INT                 |          |
|country|TEXT NOT NULL       |          |
|city   |TEXT NOT NULL       |          |
|city_id|INT UNIQUE NOT NULL |          |

## Классы для работы с базой данных

* ### DatabaseInstance - предоставляет методы для работы с БД. Конструктор принимает на вход путь к файлу файлу для БД.
    * cursor_executer(db_handler) - Принимает на вход функцию в которую передается курсор для работы с БД. Выполняет обработку ошибок и закрытие соединения и курсора БД
    * databese_init_tables() - создает структуру БД если ее нет
    * fill_cities_from_file(source_filename) - Принимает на вход путь к файлу с информацией по городам. Добавляет в БД информацию с файла если ее нет
* ### Cities - предоставляет методы для работы с таблице cities БД. Конструктор принимат на вход функцию для работы с курсором БД
    * get_city_by_city_id(city_id) - Ищет город по city_id. Возвращает список данных вида (id, country, city, city_id)
    * get_city_by_id(id) - Ищет город по id. Возвращает список данных вида (id, country, city, city_id)
    * get_city_by_name(name) - Ищет город по name. Возвращает список данных вида (id, country, city, city_id)
    * get_cities_by_country(country) - Ищет города по country. Возвращает список объекьтов типа (id, country, city, city_id)
    * update_city_by_id(id, county_name, city_name, city_id) - Изменить данные города с id. Поля county_name, city_name, city_id будут обновлены
    * update_city_by_city_id(city_id, county_name, city_name)