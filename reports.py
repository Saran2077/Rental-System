from connection import Connection

conn = Connection()

class Reports:
    def __init__(self):
        pass



    def due(self):
        column = column = "V_ID,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Services,Price"
        self.due_vehicle = conn.fetchData(table_name="Garage", columns='V_ID,BRAND,MODEL,REGISTRATIONNUMBER', condition="WHERE (Running_KM/(3000*(Services+1))) >= 1")
        conn.prettyPrint(column, self.due_vehicle)

    def vehicle_details(self):
        self.details = conn.fetchData(table_name="Garage", columns="*")
        return self.details

    def rented(self, vehicle, admin=False):
        column = "V_ID,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Services,Price"
        self.rented_cars = conn.fetchData("Garage", "*", f'WHERE TYPE = "{vehicle}" AND AvailabilityStatus = "Rented"')
        conn.prettyPrint(column, self.rented_cars)

    def available(self, vehicle, admin=False):
        column = "V_ID,Brand,Model,Year,Color,RegistrationNumber,AvailabilityStatus,Services,Price" if admin else 'V_ID,BRAND,MODEL,YEAR'
        condition = f'TYPE = "{vehicle}" AND '
        self.available_cars = conn.fetchData("Garage", columns=column, condition=f'WHERE '+ (condition if vehicle != "All" else "") +' AvailabilityStatus = "Available"')
        conn.prettyPrint(column, self.available_cars)

    def option(self):
        print("1 Vehicles that are due for service")
        print("2 Show all vehicles")
        print("3 Rented Vehicle")
        print("4 Available Vehicle")


