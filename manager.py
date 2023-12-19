from connection import Connection

conn = Connection()

class Manager:
    def __init__(self):
        pass

    def rent_vehicle(self, v_id, user_name):
        conn.update("Garage", "AvailabilityStatus", "Rented", f"V_ID = {v_id}")
        print(f'Successfully VehicleID with {v_id} is purchased by {user_name}')

    def remove_vehicle(self, v_id):
        conn.delete("Garage", f"WHERE V_ID = {v_id}")
        print(f"VehicleID with {v_id} is successfully removed")

    def search(self, v_id = "", v_name = ""):
        self.searched_vehicle = conn.search("Garage", "*", f"V_ID = {v_id}")
        print(self.searched_vehicle)
manager = Manager()
manager.search(v_id = 2)



