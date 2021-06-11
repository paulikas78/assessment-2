import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

from .rentals import Rentals
from .customers import Customers

class Inventory:
    
    def __init__(self):
        self.name = name
        self.customers = Customers.get_all_customers()
        self.rentals = Rentals.get_all_rentals()
        
    def print_inventory(self): # prints inventory of all videos.
        video = Inventory.get_inventory()
        print(f"video id: {video.id}, title: {video.title}, rating: {video.rating}, copies available: {video.copies_available}")     
                            
    @classmethod # searches inventory
    def get_inventory(cls):
        with open(path) as inventory_file:
            reader = csv.DictReader(inventory_file)
            inventory_list = []
            for row in reader:
                new_inventory = dict(row)
                inventory_list.append(new_inventory)
        return inventory_list