class Car:
    def __init__(self, car_name, model, vehicle_id, year, color, type, mileage, fuel_type):
        self.car_name = car_name
        self.model = model
        self.vehicle_id = vehicle_id
        self.year = year
        self.color = color
        self.type = type
        self.mileage = mileage
        self.fuel_type = fuel_type


class Bike:
    def __init__(self, car_name, model, vehicle_id, year, color, type, mileage):
        self.car_name = car_name
        self.model = model
        self.vehicle_id = vehicle_id
        self.year = year
        self.color = color
        self.type = type
        self.mileage = mileage


class Garage:
    def __inti__(self):
        pass
    def add(self, vehicle):
        vehicle_model = input("What is the f'vehicle' Model: ")
        vehicle_id = input("Enter the f'vehicle''s license number: ")
        vehicle_color = input("Enter the color of the f'vehicle': ")
        vehicle_top_speed = input("Top Speed of the f'vehicle': ")
        vehicle_mileage = input("Mileage of the f'vehicle': ")\
        vehicle_services = 0
        vehicle_km = 0
        
