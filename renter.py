from reports import Reports
from connection import Connection
from transaction import Transaction
from message import Message

report = Reports()
conn = Connection()
transaction = Transaction()
message = Message()

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
        self.cost = 0
        for i in conn.fetchData(table_name="Rental_History", columns="*", condition=f"WHERE USER_ID = {user_id} AND STATUS = 'Pending'"):
            v_details = conn.fetchData(table_name="Garage", columns="BRAND, MODEL, RentalPrice", condition=f"WHERE V_ID = {i[2]}")
            km = float(input(f"How many kilometers do you run this {v_details[0][0]} {v_details[0][1]}: "))
            damage = input("What extent of wear or damage has been incurred by the vehicle? (NO/LOW/MEDIUM/HIGH): ").lower()
            print(v_details)
            self.cost += transaction.cost_calculate(km=km, damage=damage, price=v_details[0][-1])
            conn.update(table_name="Rental_History", column_name="Runned_KM", set_value=km, condition=f"V_ID = {i[2]} AND USER_ID = {i[1]}")
            conn.update(table_name="Garage", column_name="AvailabilityStatus", set_value='"Available"', condition=f"V_ID = {i[2]}")
            conn.update(table_name="Garage", column_name="RUNNING_KM", set_value=f"Running_KM + {km}", condition=f"V_ID = {i[2]}")
            conn.update(table_name="Rental_History", column_name="Status", set_value='"Completed"', condition=f"s_no = {i[0]}")
            conn.update(table_name="Rental_History", column_name="Drop_Date", set_value="CURRENT_DATE()", condition=f"s_no = {i[0]}")
        print(f"Total cost with vehicle charge + fine is Rs.{self.cost}")
        print(f"Here is your remaining amount from the security deposit: {30000 - self.cost}")
        conn.update(table_name="Transaction", column_name="Cost", set_value=self.cost, condition=f'User_ID = {user_id} AND TransactionStatus = "Pending"')

    def rental_history(self, user_id):
        self.history = conn.fetchData(table_name="Rental_History", columns="*", condition=f'WHERE USER_ID = {user_id}')
        conn.prettyPrint(column="S_NO, USER_ID, V_ID, PICK_DATE, DROP_DATE, STATUS, RUNNED_KM", data=self.history)

    def renter_add(self, type, user_id):
        report.available(type)
        print("You can add upto two vehicle (One car/ One Bike)")
        self.cart = []
        while True:
            a = input("Enter the V_ID to add the vehicle to cart or confirm to book: ").lower()
            if a == "exit": break
            elif a == "confirm":
                if transaction.get_money():
                    self.column = "S_NO, USER_ID, V_ID, PICK_DATE, STATUS"
                    for i in self.cart:
                        self.sno = len(conn.fetchData(table_name="Rental_History", columns="*"))
                        query = f'{self.sno + 1}, {user_id}, {i[0]}, CURRENT_DATE(), "Pending"'
                        conn.row_add(table_name="Rental_History", columns=self.column, values=query)
                        self.rent_vehicle(v_id=i[0], user_name=user_id)
                    print(f"Total cost for purchasing {len(self.cart)} vehicle is Rs.{transaction.sum_money(','.join(map(str, self.cart)))[0][0]}")
                    return
                else:
                    print("Without paying the deposit amount we can't move to further process...")
                    return
            elif self.can_rent(self.cart, a):
                self.cart.append(a)
            else:
                print("Error you can't add two cars or two bikes")

    def extend_tenure(self):
        pass

    def vehicle_lost(self, v_id, time, place):
        self.lost_vehicle = conn.fetchData(table_name="Garage", columns="BRAND, MODEL, Color, RegistrationNumber", condition=f'WHERE V_ID = {v_id}')
        message.police(time, place, self.lost_vehicle)


    def exchange_vehicle(self):
        conn.update()

    def option(self, user_id):
        print("1 Rent a Vehicle")
        print("2 Return Vehicle")
        print("3 Rental History")
        user_has_pending = conn.fetchData(table_name="Rental_History", columns="V_ID", condition=f'WHERE USER_ID = {user_id} AND STATUS = "Pending"')
        if user_has_pending:
            print("4 Extend Tenure")
            print("5 Vehicle Lost")
            print("6 Exchange Vehicle")
        a = input("Please Enter: ").lower()
        if a == 'exit': return
        if a.isdigit() and 0 < int(a) <= 3:
            if a == '1':
                type = input("Enter which type of vehicle are you interested (Car/Bike/Both): ").lower()
                self.renter_add(type=type if type != "both" else "All", user_id=user_id)
            if a == '2':
                self.return_vehicle(user_id=user_id)
            if a == '3': self.rental_history(user_id=user_id)
        elif user_has_pending and int(a) <= 6:
            if a == '4':
                self.extend_tenure()
            if a == '5':
                lost = input("Enter the V_ID of the lost Vehicle: ")
                for i in user_has_pending:
                    if i[0] == lost:
                        time = input("What time the vehicle get lost? ")
                        place = input("Where did the vehicle get lost? ")
                        self.vehicle_lost(time, place, lost)
                        break
                else:
                    print("The provided vehicle is not purchased by You...")
            if a == '6':
                type = input("Enter which type of vehicle are you interested (Car/Bike/Both): ").lower()
                self.renter_add(type=type if type != "both" else "All", user_id=user_id)
                v_id = input("What vehicle are you want to exchange from? ")
                self.exchange_vehicle(v_id)
        else:
            print("Enter a valid option!")
            self.option(user_id=user_id)


renter = Renter()
renter.option(1)



