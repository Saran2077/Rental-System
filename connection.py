import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import os
import time

class Connection:
    def __init__(self):
        self.create_server_connection = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                passwd = "2580",
                database = "Rental_System"
        )
        self.cursor = self.create_server_connection.cursor()

    def row_add(self, table_name, values, columns=""):
        self.cursor.execute(f"INSERT INTO {table_name} "+(f"({columns})" if columns != "" else "") +f"VALUES ({values});")
        self.create_server_connection.commit()

    def count(self, table_name, column_name):
        self.column_count = self.cursor.execute(f"SELECT {column_name} FROM {table_name};")
        return 0 if self.column_count == None else self.column_count

    def fetchData(self, table_name, columns, condition=""):
        print((f"SELECT {columns} FROM {table_name} {condition};"))
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

    def prettyPrint(self, column, data):
        my_Table = PrettyTable(column.split(','))
        for i in data:
            my_Table.add_row([*i])
        print(my_Table)

    # def clearScreen(self):
    #     os.system('cls')

    def clearScreen(self, duration=1, frames_per_second=10):
        total_frames = duration * frames_per_second
        for frame in range(total_frames):
            os.system('cls')
            print("Clearing Screen: {:.2%}".format(frame / total_frames))
            time.sleep(1 / frames_per_second)
            os.system('cls')


# create_server_connection = mysql.connector.connect(
#                 host = "127.0.0.1",
#                 user = "root",
#                 passwd = "2580",
#                 database = "Rental_System"
#         )


