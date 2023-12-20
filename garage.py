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

    def remove_vehicle(self, v_id):
        conn.delete("Garage", f"WHERE V_ID = {v_id}")
        print(f"VehicleID with {v_id} is successfully removed")

    def search(self, v_id):
        self.searched_vehicle = conn.search("Garage", "*", f"V_ID = {v_id}")
        print(self.searched_vehicle)

    def option(self):
        print("1 Add a Vehicle")
        print("2 Remove a Vehicle")
        print("3 Search a Vehicle")
        print("4 Show Garage")
        self.choice = input("Please Enter: ")
        if self.choice.lower() == 'exit': return
        if self.choice.isdigit() == False: print("Enter a number")
        if int(self.choice) >= 0 and int(self.choice) <= 4:
            if self.choice == '1':
                type = input("What vehicle do you want to add (Car/Bike): ")
                if type.lower() == "car" or type.lower() == "bike": self.add(type)
                else: print("Wrong input..")
                self.option()
            elif self.choice == '2':
                v_id = input("Please Enter a V_ID to remove the vehicle: ")
                if v_id <= vehicle_count and v_id > 0 and conn.fetchData(columns="AvailabilityStatus", table_name="Garage", condition=f"WHERE V_ID = {v_id}")[0] == ("Available"):
                    self.remove_vehicle(v_id)
                else:
                    print("Not a valid v_id")
                    self.option()
            elif self.choice == '3':
                v_id = input("Enter a V_ID to search: ")
                if int(v_id) <= vehicle_count and int(v_id) > 0 and conn.fetchData(columns="AvailabilityStatus", table_name="Garage", condition=f"WHERE V_ID = {v_id}")[0][0] == ("Available"):
                    self.search(v_id)
                else:
                    print("Not a valid v_id")
                    self.option()
            elif self.choice == '4':
                self.data = conn.fetchData(table_name="Garage", columns="*", condition="")
                print(self.data)
            else:
                print("Please enter a valid option")
                self.option()
        else:
            print("Wrong input .. ")
            self.option()





