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
        self.available_cars = conn.fetchData("Garage", admin_column if admin else user_column, f'WHERE TYPE = "{vehicle}" AND AvailabilityStatus = "Available"')
        print(self.available_cars)



reports = Reports()
reports.available("Car")
