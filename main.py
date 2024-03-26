'''
    Подключаемся к Postgres
'''
import psycopg2
from config import dbname, user, password, host, port


try:
    # connection = psycopg2.connect("dbname=postgres user=postgres password=postgrespython1 host=localhost port=5440")
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    connection.autocommit = True
    # cur = connection.cursor()

    # create table
    # with connection.cursor() as cur:
    #     cur.execute(
    #         "CREATE TABLE person (id SERIAL PRIMARY KEY, name VARCHAR(50), age INT);"
    #     )
        # print(f"Server version: {cur.fetchone()}")

    # insert into
    # with connection.cursor() as cur_create:
    #     cur_create.execute(
    #         """INSERT INTO person (name, age) VALUES ('Asadullah', 18);"""
    #     )
    #     print(f"[INFO] Table created successfully")

    # select
    # with connection.cursor() as cur_select:
    #     cur_select.execute(
    #         "SELECT * FROM person;"
    #     )
    #     print(f'Objects from databasec: {cur_select.fetchone()[:]}')

    # drop table
    with connection.cursor() as cur_drop:
        cur_drop.execute(
            """DROP TABLE person;"""
        )
        print('Success drop tables')

except Exception as ex:
    print(f'[INFO] Error while working with PostgreSQL, {ex}')
finally:
    if connection:
        # cur.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')

