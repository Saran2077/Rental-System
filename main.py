# import sign
from garage import Car, Bike
import json


with open('data.json', 'r') as file:
    data = json.load(file)
    print(data["saranjamespond123@gmail.com"]["name"])