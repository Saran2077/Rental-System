from sign import *
from garage import Garage
from reports import Reports
from renter import Renter

report = Reports()
garage = Garage()
renter = Renter()


admin = [1]
id = login()
if id in admin:
    print("Please enter 1 or 2")
    print("1 Vehicle Inventory")
    print("2 Reports")
    a = input("Please Enter: ")
    if a.isdigit() and a == '1':
        garage.option()
    if a.isdigit() and a == '2':
        report.option()
else:
    renter.option(user_id=id)



