import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

from .rentals import Rentals
from .customers import Customers


class Inventory:
    
    def __init__(self, customers, rentals):
        self.name = name
        self.customers = Customers.get_all_customers()
        self.rentals = Rentals.get_all_rentals()
        
    def all_customers(self):
        return self.customers
    
    def find_customer_with_id(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
            else:
                print(f"{id} not found")
                return None
            
    def assign_rental_to_customer(self):
        customer_id = Inventory.get_all_customers()
        for value in customer_id:
            for customer in self.customers:
                if int(customer.id) == int(value["customer_id"]):
                    for rental in self.rentals:
                        print(f"rental: {rental}")
                        if rental.id == int(value["rental_id"]):
                            customer.rental = rental
                            print(f"customer rental(s): {customer.rental.first_name} {customer.rental.last_name}")
                            
    @classmethod
    def get_inventory(cls):
        with open(path) as inventory_file:
            reader = csv.DictReader(inventory_file)
            inventory_list = []
            for row in reader:
                new_inventory = dict(row)
                inventory_list.append(new_inventory)
        return inventory_list