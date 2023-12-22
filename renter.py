from reports import Reports
from connection import Connection

report = Reports()
conn = Connection()

class Renter:
    def __init__(self):
        pass

    def rent_vehicle(self, v_id, user_name):
        conn.update("Garage", "AvailabilityStatus", '"Rented"', f"V_ID = {v_id}")
        print(f'Successfully VehicleID with {v_id} is purchased by {user_name}')

    def can_rent(self, cart, new_item):
        if conn.fetchData(table_name="Garage", columns="AvailabilityStatus", condition=f'WHERE V_ID = {new_item}')[0][0] == 'Available':
            if len([*cart, new_item]) <= 2:
                if cart == [] or conn.fetchData(table_name="Garage", columns="Type", condition=f'WHERE V_ID = {cart[0]}') != conn.fetchData(table_name="Garage", columns="Type", condition=f'WHERE V_ID = {new_item}'):
                    return True
        return False

    def return_vehicle(self, user_id):
        for i in conn.fetchData(table_name="Rental_History", columns="*", condition=f"WHERE USER_ID = {user_id} AND Rental_Status = 'Pending'"):
            conn.update("Garage", "AvailabilityStatus", '"Available"', f"V_ID = {i[2]}")
            conn.update(table_name="Rental_History", column_name="Rental_Status", set_value='"Completed"', condition=f"s_no = {i[0]}")
            conn.update(table_name="Rental_History", column_name="Drop_Date", set_value="CURRENT_DATE()", condition=f"s_no = {i[0]}")

    def renter_add(self, type, user_id):
        report.available(type)
        print("You can add upto two vehicle (One car/ One Bike)")
        self.cart = []
        while True:
            a = input("Enter the V_ID to add the vehicle to cart or confirm to book: ").lower()
            if a == "exit": break
            if a == "confirm":
                self.column = "S_NO, USER_ID, V_ID, RENT_DATE, RENTAL_STATUS"
                for i in self.cart:
                    self.sno = len(conn.fetchData(table_name="Rental_History", columns="*"))
                    query = f'{self.sno + 1}, {user_id}, {i[0]}, CURRENT_DATE(), "Pending"'
                    conn.row_add(table_name="Rental_History", columns=self.column, values=query)
                    self.rent_vehicle(v_id=i[0], user_name=user_id)
                break
            if self.can_rent(self.cart, a):
                self.cart.append(a)
            else:
                print("Error you cant add two cars or two bikes")
renter = Renter()
renter.return_vehicle(1)


