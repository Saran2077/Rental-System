from connection import Connection

conn = Connection()
vehicle_count = len(conn.fetchData("Garage","*"))

class Garage:
    def __inti__(self):
        pass
    def add(self, vehicle):
        vehicle_questions = [
            f"What is the Brand of the {vehicle}",
            f"What is the Model of the {vehicle}",
            f"Manufactured Year",
            f"Color of the {vehicle}",
            f"Registration Number"
        ]

        data = f'{vehicle_count+1}'+',"'+f'{vehicle}'+'"'
        i = 0
        while i < 5:
            a = input(vehicle_questions[i]+": ")
            if a.replace(" ","") == "":
                continue
            i += 1
            data += ',' +'"'+a+'"'
        if i == 5:
            data += ',"'+"Available"+'",'+'0'+','+'0'+','+input(f"Enter the Price of the {vehicle} per day: ")
            conn.row_add("Garage", data)




    # def returned(self):

garage = Garage()
garage.add("Car")