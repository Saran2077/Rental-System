import mysql.connector
from mysql.connector import Error

class Connection:
    def __inti__(self):
        self.create_server_connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd = "1234",
                database = "Rental_System"
        )
        self.cursor = self.create_server_connection.cursor()

    def row_add(self, table_name, values):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES {values}")
