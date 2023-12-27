from connection import Connection

conn = Connection()

class Reports:
    def __init__(self, admin=False):
        self.admin = admin


    def due(self):
        self.due_vehicle = conn.fetchData(table_name="Garage", columns='V_ID,BRAND,MODEL,TYPE,REGISTRATIONNUMBER', condition='WHERE (Running_KM/(3000*(Services+1))) >= 1 AND AvailabilityStatus != "Lost"')
        return self.due_vehicle

    def print_due(self):
        column = column = "V_ID,Brand,Model,Type,RegistrationNumber"
        conn.prettyPrint(column, self.due())

    def vehicle_details(self):
        self.details = conn.fetchData(table_name="Garage", columns="*")
        conn.prettyPrint(column="V_ID,Type,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Runnig_KM,Services,Price", data=self.details)

    def rented(self, vehicle):
        column = "V_ID,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Services,Price"
        self.rented_cars = conn.fetchData("Garage", "*", f'WHERE TYPE = "{vehicle}" AND AvailabilityStatus = "Rented"')
        conn.prettyPrint(column, self.rented_cars)

    def available(self, vehicle, admin=False):
        column = "V_ID,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Services,RentalPrice" if admin else 'V_ID,BRAND,MODEL,YEAR'
        condition = f'TYPE = "{vehicle}" AND '
        self.available_cars = conn.fetchData("Garage", columns=column, condition=f'WHERE '+ (condition if vehicle != "All" else "") +f'AvailabilityStatus = "Available" AND V_ID NOT IN (SELECT V_ID FROM Garage WHERE ((Running_KM/(3000*(Services+1))) >= 1) AND Type = "Car") OR (Running_KM/(1500*(Services+1))) >= 1) AND Type = "Bike")')
        conn.prettyPrint(column, self.available_cars)

    def send_due(self):
        self.dued_vehicle = self.due()
        for i in self.dued_vehicle:
            conn.update(table_name="Garage", column_name="Services", set_value="Services+1", condition=f"V_ID = {i[0]}")

    def lost_vehicles(self):
        self.lost = conn.fetchData(table_name="Garage", columns="*", condition='WHERE AvailabilityStatus = "Lost"')
        conn.prettyPrint(column="V_ID,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Services,RentalPrice", data=self.lost)

    def option(self):
        conn.clearScreen()
        print("You are in Reports.")
        print("1 Vehicles that are due for service")
        print("2 Show all vehicles")
        print("3 Rented Vehicle")
        print("4 Available Vehicle")
        print("5 To send Vehicles for due")
        print("6 Lost Vehicles")
        a = input("Please Enter: ").lower()
        if a == 'exit': return
        if a.isdigit() and int(a) > 0 and int(a) <= 6:
            if a == '1': self.print_due()
            if a == '2': self.vehicle_details()
            if a == '3':
                s = input("Bike/Car/Both: ").lower()
                if s not in ["bike", "car", "both"]:
                    self.option()
                else: self.rented(s if s != "both" else "All")
            if a == '4':
                s = input("Bike/Car/Both: ").lower()
                if s not in ("bike", "car", "both"):
                    self.option()
                else:
                    self.available(vehicle=s if s != "both" else "All", admin=True)
            if a == '5':
                self.send_due()
            if a == '6':
                self.lost_vehicles()
        else:
            print("Please Enter a valid option!")
            self.option()
        is_continue = input("Do you want to Continue: (Y/N) ").lower()
        if is_continue == 'y':
            if self.option() == None:
                return
