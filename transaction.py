from connection import Connection

conn = Connection()

class Transaction:
    def __init__(self):
        pass

    def get_money(self):
        print("Each Borrower has deposited 30000 rupees Initially into the Rent Service as a Caution deposit .\nThe amount will be refunded on returning the vehicle.\nThe Amount will be reduced if there is any damage or loss of vehicle")
        a = input("Please deposit a amount of Rs.30,000 for security purpose: ")
        if a.isdigit() and a == "30000":
            return True
        print("Deposit amount for further process...")
        return False

    def sum_money(self, v_id):
        self.totalMoney = conn.fetchData(table_name="Garage", columns="SUM(RentalPrice)", condition=f"WHERE V_ID IN ({v_id})")
        return self.totalMoney

    def cost_calculate(self, km, damage, price):
        if km > 500:
            price *= 1.15
        if damage == 'low':
            price *= 1.20
        if damage == 'medium':
            price *= 1.50
        if damage == 'high':
            price *= 1.75
        return int(price)



