from connection import Connection

conn = Connection()

class Reports:
    def __init__(self):
        pass

    def due(self):
        self.due_vehicle = conn.fetchData(table_name="Garage", columns='V_ID,BRAND,MODEL,REGISTRATIONNUMBER', condition="WHERE (Running_KM/(3000*(Services+1))) >= 1")
        return self.due_vehicle

    def vehicle_details(self):
        self.details = conn.fetchData(table_name="Garage", columns="*")
        return self.details

    def rented(self, vehicle, admin=False):
        self.rented_cars = conn.fetchData("Garage", "*", f'WHERE TYPE = "{vehicle}" AND AvailabilityStatus = "Rented"')
        print(self.rented_cars)

    def available(self, vehicle, admin=False):
        admin_column = "*"
        user_column = 'V_ID,BRAND,MODEL,YEAR'
        condition = f'TYPE = "{vehicle}" AND '
        self.available_cars = conn.fetchData("Garage", admin_column if admin else user_column, f'WHERE '+ (condition if vehicle != "All" else "") +' AvailabilityStatus = "Available"')
        print(self.available_cars)

    def option(self):
        print("1 Vehicles that are due for service")
        print("2 Show all vehicles")
        print("3 Rented Vehicle")
        print("4 Available Vehicle")


reports = Reports()
