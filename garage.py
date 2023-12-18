from connection import Connection

conn = Connection()
vehicle_count = len(conn.fetchData("Garage","*"))

class Garage:
    def __inti__(self):
        pass
    def add(self, vehicle):
        vehicle_questions = [
            f"What if the Brand of the {vehicle}",
            f"What is the Model of the {vehicle}",
            f"Manufactured Year",
            f"Color of the {vehicle}",
            f"Registration Number"
        ]

        data = f'{vehicle_count}'+',"'+f'{vehicle}'+'"'
        i = 0
        while i < 5:
            a = input(vehicle_questions[i]+": ")
            if a.replace(" ","") == "":
                continue
            i += 1
            data += ',' +'"'+a+'"'
        if i == 5:
            data += ',"'+"Available"+'",'+'0'+','+'0'
            print(data)
            conn.row_add("Garage", data)

    def available(self, vehicle, admin=False):
        admin_column = "*"
        user_column = 'V_ID,BRAND,MODEL,YEAR'
        self.available_cars = conn.fetchData("Garage", admin_column if admin else user_column, f'WHERE TYPE = "{vehicle}" AND AvailabilityStatus = "Available"')
        print(self.available_cars)
    # def rented(self):
    #
    # def due(self):
    #
    #
    # def due_send(self):
    #
    #
    # def returned(self):
    #
    #
    # def


garage = Garage()
garage.available("Car")