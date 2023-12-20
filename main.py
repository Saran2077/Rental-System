from sign import *
from garage import Garage
from reports import Reports

report = Reports()
garage = Garage()

# if login():
while True:
    print("Please enter 1 or 2")
    print("1 Vehicle Inventory")
    print("2 Reports")
    a = input()
    if a.lower() == 'exit': break
    report.option()


