import os
import mysql.connector


class Mysql_connector:
    def __init__(self):
        self.database = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )

    def execute_query(self, query):
        cursor_object = self.database.cursor()
        cursor_object.execute(query)

        result = cursor_object.fetchall()
        return result

    def __del__(self):
        self.database.close()