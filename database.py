import sqlite3


def connect_database():

    connection = sqlite3.connect(
        "users.db"
    )

    return connection


def create_table():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
        """
    )

    connection.commit()

    connection.close()


def add_user(name, email):

    connection = connect_database()

    cursor = connection.cursor()

    query = (
        "INSERT INTO users (name, email) "
        "VALUES ('"
        + name
        + "', '"
        + email
        + "')"
    )

    cursor.execute(query)

    connection.commit()

    connection.close()