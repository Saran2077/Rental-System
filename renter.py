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
        self.total_cost = 0
        for i in conn.fetchData(table_name="RentalTransactions", columns="*", condition=f"WHERE USER_ID = {user_id}"):
            self.sno = conn.fetchData(table_name="Rental_History", columns="*")
            v_details = conn.fetchData(table_name="Garage", columns="BRAND, MODEL, RentalPrice", condition=f"WHERE V_ID = {i[2]}")
            km = float(input(f"How many kilometers do you run this {v_details[0][0]} {v_details[0][1]}: "))
            damage = input("What extent of wear or damage has been incurred by the vehicle? (NO/LOW/MEDIUM/HIGH): ").lower()
            self.cost = transaction.cost_calculate(km=km, damage=damage, price=v_details[0][-1]*i[4])
            print(str(i[3]))
            conn.row_add(table_name="Rental_History", values=f'{len(self.sno)}, {i[1]}, {i[2]}, "{str(i[3])}", CURRENT_DATE(), {km}, {self.cost}')
            conn.update(table_name="Garage", column_name="AvailabilityStatus", set_value='"Available"', condition=f"V_ID = {i[2]}")
            conn.update(table_name="Garage", column_name="RUNNING_KM", set_value=f"Running_KM + {km}", condition=f"V_ID = {i[2]}")
            self.total_cost += self.cost
        print(f"Total cost with vehicle charge + fine is Rs.{self.total_cost}")
        print(f"Here is your remaining amount from the security deposit: {30000 - self.total_cost}")
        conn.delete(table_name="RentalTransactions", condition=f"WHERE USER_ID = {user_id}")

    def rental_history(self, user_id):
        self.history = conn.fetchData(table_name="Rental_History", columns="*", condition=f'WHERE USER_ID = {user_id}')
        conn.prettyPrint(column="S_NO, USER_ID, V_ID, PICK_DATE, DROP_DATE, RUNNED_KM, Price", data=self.history)

    def renter_add(self, type, user_id):
        report.available(type)
        print("You can add upto two vehicle (One car/ One Bike)")
        self.cart = []
        while True:
            a = input("Enter the V_ID to add the vehicle to cart or confirm to book: ").lower()
            if a == "exit": break
            elif a == "confirm":
                if transaction.get_money():
                    daysRented = input("How many days do you want to rent the vehicle: ")
                    self.column = "TransactionID, USER_ID, V_ID, Rent_Date, DaysRented, ExtensionsLeft, SecurityDeposit"
                    for i in self.cart:
                        self.sno = len(conn.fetchData(table_name="RentalTransactions", columns="*"))
                        query = f'{self.sno + 1}, {user_id}, {i[0]}, CURRENT_DATE(), {daysRented}, 2, true'
                        conn.row_add(table_name="RentalTransactions", columns=self.column, values=query)
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

    def extend_tenure(self, user_id, v_id, days):
        conn.update(table_name="RentalTransactions", column_name="DaysRented", set_value=f"DaysRented + {days}", condition=f"V_ID = {v_id} AND User_ID = {user_id}")
        conn.update(table_name="RentalTransactions", column_name="ExtensionsLeft", set_value=f"ExtensionsLeft - {days}", condition=f"V_ID = {v_id} AND User_ID = {user_id}")
        print("You have successfully extended the Vehicle Tensure...")



    def vehicle_lost(self, v_id, time, place):
        self.lost_vehicle = conn.fetchData(table_name="Garage", columns="BRAND, MODEL, Color, RegistrationNumber", condition=f'WHERE V_ID = {v_id}')
        message.police(time, place, self.lost_vehicle)


    # def exchange_vehicle(self):
    #     conn.update(table_name="RentalTransactions", column_name="DaysRented", set_value=f"DaysRented + {}")

    def option(self, user_id):
        print("1 Rent a Vehicle")
        print("2 Rental History")
        user_has_pending = conn.fetchData(table_name="RentalTransactions", columns="V_ID", condition=f'WHERE USER_ID = {user_id}')
        if user_has_pending:
            print("3 Return Vehicle")
            print("4 Extend Tenure")
            print("5 Vehicle Lost")
            print("6 Exchange Vehicle")
        a = input("Please Enter: ").lower()
        if a == 'exit': return
        if a.isdigit() and 0 < int(a) <= 2:
            if a == '1':
                type = input("Enter which type of vehicle are you interested (Car/Bike/Both): ").lower()
                self.renter_add(type=type if type != "both" else "All", user_id=user_id)
            if a == '2': self.rental_history(user_id=user_id)
        elif user_has_pending and int(a) <= 6:
            if a == '3':
                self.return_vehicle(user_id=user_id)
            if a == '4':
                self.transaction_data = conn.fetchData(table_name="RentalTransactions", columns="Garage.V_ID, BRAND, MODEL, COLOR, DaysRented, ExtensionsLeft", condition=f"JOIN Garage ON Garage.V_ID = RentalTransactions.V_ID WHERE USER_ID = {user_id} ORDER BY Garage.V_ID")
                conn.prettyPrint(column="V_ID, BRAND, MODEL, COLOR, DaysRented, ExtensionsLeft", data=self.transaction_data)
                choose = input("Which vehicle do you to extend? ")
                print(self.transaction_data)
                if int(choose) in [i[0] for i in self.transaction_data]:
                    days = input("You can extend a day or two: (1/2) ")
                    if days.isdigit() and int(days) > 1 and int(days) <= self.transaction_data[0 if self.transaction_data[0][-1] else 1][-1]:
                        self.extend_tenure(user_id, choose, days)
                    else:
                        print(f"You cant extend {choose} days...")
                        self.option(user_id)
                else:
                    print("You entered a wrong v_id...")

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




