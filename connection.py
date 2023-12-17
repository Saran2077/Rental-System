import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self):
        self.create_server_connection = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                passwd = "2580",
                database = "Rental_System"
        )
        self.cursor = self.create_server_connection.cursor()

    def row_add(self, table_name, values):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({values});")
        self.create_server_connection.commit()

    def count(self, table_name, column_name):
        self.column_count = self.cursor.execute(f"SELECT {column_name} FROM {table_name};")
        return 0 if self.column_count == None else self.column_count

    def fetchData(self, table_name, columns, condition=""):
        self.cursor.execute(f"SELECT {columns} FROM {table_name};")
        self.data = self.cursor.fetchall()
        return self.data
#
# create_server_connection = mysql.connector.connect(
#                 host = "127.0.0.1",
#                 user = "root",
#                 passwd = "2580",
#                 database = "Rental_System"
#         )
# cursor = create_server_connection.cursor()
# table_name = "User_Details"
# values = '1,"saran","saran@gmail.com","M","9092786919","9999 0000 9999","saran21","Saran123"'
#
# print(f"INSERT INTO {table_name} VALUES ({values});")