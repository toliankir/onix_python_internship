from abc import abstractmethod
import csv
import logging
import sqlite3

DATA_CSV_FILENAME = "task5/full_city_list.txt"
DB_FILE = "task5/database.db"


class DatabaseInstance:
    def __init__(self, connection_string: str):
        self.__connection_string = connection_string
        logging.info("Database connection init: %s" % connection_string)

    def cursor_executer(self, db_handler):
        try:
            with sqlite3.connect(self.__connection_string) as connection:
                cursor = connection.cursor()
                data = db_handler(cursor)
                cursor.close()
                return data
        except sqlite3.DatabaseError as e:
            print(e)

    def databese_init_tables(self):
        def db_handler(cursor): return cursor.execute("""CREATE TABLE IF NOT EXISTS "cities" (
            "id" INTEGER PRIMARY KEY, 
            "country" TEXT NOT NULL, 
            "city" TEXT NOT NULL, 
            "city_id" INT UNIQUE NOT NULL)""")
        self.cursor_executer(db_handler)
        logging.debug("""Database table "cities" init""")

    def fill_cities_from_file(self, source_filename):
        def check_city_data(row: dict):
            if (row.get("Country") != None and row.get("City") != None and row.get("CityId") != None):
                return True
            return False

        def get_cities_data_from_file(source_filename):
            with open(source_filename, "r") as file:
                csv_data = csv.DictReader(file, delimiter=";")
                for row in csv_data:
                    data = dict(row)
                    if (not check_city_data(data)):
                        continue
                    yield (row.get("Country"), row.get("City"), row.get("CityId"))

        cities_list = get_cities_data_from_file(source_filename)

        def db_handler(cursor):
            sql_raw = """INSERT OR IGNORE INTO "cities" ("country", "city", "city_id") VALUES(?, ?, ?)"""
            return cursor.executemany(sql_raw, cities_list)

        self.cursor_executer(db_handler)
        logging.debug("""Check file %s. Add data to database""" % source_filename)


class Cities:
    def __init__(self, cursor_executer):
        self.__cursor_executer = cursor_executer

    def get_city_by_city_id(self, city_id):
        def db_handler(cursor):
            sql_raw = """SELECT "id",  "country", "city", "city_id" FROM "cities" WHERE "city_id" = ?"""
            cursor.execute(sql_raw, (city_id,))
            row = cursor.fetchone()
            return row
        logging.debug("""Get city by city_id %s""" % city_id)
        return self.__cursor_executer(db_handler)

    def get_city_by_id(self, id):
        def db_handler(cursor):
            sql_raw = """SELECT "id",  "country", "city", "city_id" FROM "cities" WHERE "id" = ?"""
            cursor.execute(sql_raw, (id,))
            row = cursor.fetchone()
            return row
        logging.debug("""Get city by id %s""" % id)
        return self.__cursor_executer(db_handler)

    def get_city_by_name(self, name):
        def db_handler(cursor):
            sql_raw = """SELECT "id",  "country", "city", "city_id" FROM "cities" WHERE "city" = ?"""
            cursor.execute(sql_raw, (name,))
            row = cursor.fetchone()
            return row
        logging.debug("""Get city by name %s""" % name)
        return self.__cursor_executer(db_handler)

    def get_cities_by_country(self, country):
        def db_handler(cursor):
            sql_raw = """SELECT "id",  "country", "city", "city_id" FROM "cities" WHERE "country" = ?"""
            cursor.execute(sql_raw, (country,))
            rows = cursor.fetchall()
            return rows
        logging.debug("""Get cities by country %s""" % country)
        return self.__cursor_executer(db_handler)

    def update_city_by_id(self, id, county_name, city_name, city_id):
        def db_handler(cursor):
            sql_raw = """UPDATE "cities" SET "country"=?, "city"=?, "city_id"=? WHERE "id" = ?"""
            cursor.execute(sql_raw, (county_name, city_name, city_id,  id))
        logging.debug("""Update city by id %s. Set county_name="%s", city_name="%s", city_id="%s\"""" % (id, county_name, city_name, city_id))
        self.__cursor_executer(db_handler)

    def update_city_by_city_id(self, city_id, county_name, city_name):
        def db_handler(cursor):
            sql_raw = """UPDATE "cities" SET "country"=?, "city"=? WHERE "city_id" = ?"""
            cursor.execute(sql_raw, (county_name, city_name, city_id))
        logging.debug("""Update city by city_id %s. Set county_name=\"%s\", city_name=\"%s\"""" % (city_id, county_name, city_name))
        self.__cursor_executer(db_handler)


logging.basicConfig(level=logging.DEBUG)

db = DatabaseInstance(DB_FILE)
db.databese_init_tables()
db.fill_cities_from_file(DATA_CSV_FILENAME)
cities = Cities(db.cursor_executer)

test_id = 26;
test_city_name = "Benidorm"
test_cities_contry = "Ukraine"

print("\033[93mGet city by city_id:\033[0m %s" % test_id)
print(cities.get_city_by_city_id(test_id))

print("\n\033[93mGet city id:\033[0m %s" % test_id)
city = cities.get_city_by_id(test_id)
print(cities.get_city_by_id(test_id))

print("\n\033[93mUpdate city by id:\033[0m %s" % test_id)
cities.update_city_by_id(26, "%s_updated"%city[1], "%s_updated"%city[2], city[3]*1000)

print("\n\033[93mGet city id:\033[0m %s" % test_id)
print(cities.get_city_by_id(test_id))

print("\n\033[93mUpdate city by id(Retrun correct data):\033[0m %s" % test_id)
cities.update_city_by_id(26, city[1], city[2], city[3])

print("\n\033[93mGet city id:\033[0m %s" % test_id)
print(cities.get_city_by_id(test_id))

print("\n\033[93mGet city by name:\033[0m %s" % test_city_name)
print(cities.get_city_by_name(test_city_name))

print("\n\033[93mGet cities by country:\033[0m %s" % test_cities_contry)
for city in cities.get_cities_by_country(test_cities_contry):
    print(city)
