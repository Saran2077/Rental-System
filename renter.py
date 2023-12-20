from reports import Reports

report = Reports()

class Renter:
    def __init__(self):
        pass

    def can_rent(self, cart, new_item):
        if len([*cart, new_item]) >= 2:

            return False

    def cart(self):
        pass

    def renter_add(self, type):
        print(report.available(type))


renter = Renter()
renter.renter_add("Car")

