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
        print(values)
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({values});")
        self.create_server_connection.commit()

    def count(self, table_name, column_name):
        self.column_count = self.cursor.execute(f"SELECT {column_name} FROM {table_name};")
        return 0 if self.column_count == None else self.column_count

    def fetchData(self, table_name, columns, condition=""):
        self.cursor.execute(f"SELECT {columns} FROM {table_name} {condition};")
        self.data = self.cursor.fetchall()
        return self.data

    def execute(self, table_name, column_name, condition=""):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name} {condition}")
        self.create_server_connection.commit()

    def update(self, table_name, column_name, set_value, condition):
        self.cursor.execute(f'UPDATE {table_name} SET {column_name} = {set_value} WHERE {condition}')
        self.create_server_connection.commit()

    def delete(self, table_name, condition):
        self.cursor.execute(f'DELETE FROM {table_name} {condition}')
        self.create_server_connection.commit()

    def search(self, table_name, column_name, condition):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE {condition}")
        self.searched_vehice = self.cursor.fetchall()
        return self.searched_vehice


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
