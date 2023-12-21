from reports import Reports
from connection import Connection

report = Reports()
conn = Connection()

class Renter:
    def __init__(self):
        pass

    def can_rent(self, cart, new_item):
        if len([*cart, new_item]) <= 2:
            if cart == [] or cart[-1] != new_item[-1]:
                return True
        return False

    def cart(self):
        pass

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
                break
            if self.can_rent(self.cart, a):
                self.cart.append(a)
            else:
                print("Error you cant add two cars or two bikes")
renter = Renter()
renter.renter_add("All", 1)


