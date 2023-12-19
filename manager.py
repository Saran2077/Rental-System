from connection import Connection

conn = Connection()

class Manager:
    def __init__(self):
        pass

    def rent_vehicle(self, v_id, user_name):
        conn.update("Garage", "AvailabilityStatus", '"Rented"', f"V_ID = {v_id}")
        print(f'Successfully VehicleID with {v_id} is purchased by {user_name}')

    def remove_vehicle(self, v_id):
        conn.delete("Garage", f"WHERE V_ID = {v_id}")
        print(f"VehicleID with {v_id} is successfully removed")

    def search(self, v_id = "", v_name = ""):
        self.searched_vehicle = conn.search("Garage", "*", f"V_ID = {v_id}")
        print(self.searched_vehicle)

    def due(self):
        self.due_vehicle = conn.fetchData(table_name="Garage", columns='V_ID,BRAND,MODEL,REGISTRATIONNUMBER', condition="WHERE (Running_KM/(3000*(Services+1))) >= 1")
        return self.due_vehicle

    def send_due(self):
        self.dued_vehicle = self.due()
        for i in self.dued_vehicle:
            conn.update(table_name="Garage", column_name="Services", set_value="Services+1", condition=f"V_ID = {i[0]}")

manager = Manager()
print(manager.due())



