from connection import Connection

conn = Connection()
vehicle_count = [item[0] for item in conn.fetchData(table_name="Garage", columns="V_ID")]


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

        data = f'{len(vehicle_count)+1}'+',"'+f'{vehicle}'+'"'
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
            vehicle_count.append(data.split(',')[0])
            print("Successfully Vehicle is added to our garage...")

    def remove_vehicle(self, v_id):
        conn.delete("Garage", f"WHERE V_ID = {v_id}")
        print(f"VehicleID with {v_id} is successfully removed")

    def search(self, v_id):
        self.searched_vehicle = conn.search("Garage", "*", f"V_ID = {v_id}")
        conn.prettyPrint(column="V_ID,Type,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Running_KM,Services,Price", data=self.searched_vehicle)

    def vehicle_details(self):
        self.details = conn.fetchData(table_name="Garage", columns="*")
        conn.prettyPrint(column="V_ID,Type,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Runnig_KM,Services,Price", data=self.details)


    def option(self):
        conn.clearScreen()
        print("You are in Vehicle Inventory.")
        print("1 Add a Vehicle")
        print("2 Remove a Vehicle")
        print("3 Search a Vehicle")
        print("4 Show Garage")
        self.choice = input("Please Enter: ")
        if self.choice.lower() == 'exit': return
        if self.choice.isdigit() and int(self.choice) >= 0 and int(self.choice) <= 4:
            if self.choice == '1':
                type = input("What vehicle do you want to add (Car/Bike): ")
                if type.lower() == "car" or type.lower() == "bike": self.add(type)
                else: print("Please enter a valid option")
                self.option()
            elif self.choice == '2':
                v_id = input("Please Enter a V_ID to remove the vehicle: ")
                if int(v_id) in vehicle_count and conn.fetchData(columns="AvailabilityStatus", table_name="Garage", condition=f"WHERE V_ID = {v_id}")[0][0] == "Available":
                    self.remove_vehicle(v_id)
                elif int(v_id) in vehicle_count and conn.fetchData(columns="AvailabilityStatus", table_name="Garage", condition=f"WHERE V_ID = {v_id}")[0][0] == "Rented":
                    print("Kindly we can't remove this vehicle from our garage it is rented by customer...")
                elif int(v_id) in vehicle_count and conn.fetchData(columns="AvailabilityStatus", table_name="Garage", condition=f"WHERE V_ID = {v_id}")[0][0] == "Lost":
                    print("Sorry sir this vehicle is currently lost...")
                else:
                    print(f"We dont have any vehicle with this V_ID = {v_id}")
            elif self.choice == '3':
                v_id = input("Enter a V_ID to search: ")
                if int(v_id) in vehicle_count and conn.fetchData(columns="AvailabilityStatus", table_name="Garage", condition=f"WHERE V_ID = {v_id}")[0][0] != ("Lost"):
                    self.search(v_id)
                else:
                    print(f"We dont have any vehicle with this V_ID = {v_id}")
            elif self.choice == '4':
                self.vehicle_details()
            else:
                print("Please enter a valid option")
        else:
            print("Please enter a valid option")
        is_continue = input("Do you want to Continue: (Y/N) ").lower()
        if is_continue == 'y':
            if self.option() == None:
                return


garage = Garage()



