import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

from modules.customers import Customers
from modules.inventory import Inventory

class Interface:    # creates interface for customers to use, regarding their respective accounts.
    customers_list = []

    menu_options = ['\n1. View video inventory', '\n2. View customer\'s rented videos', '\n3. Rent videos', '\n4. Return videos', '\n5. Add new customer', '\n6. Exit']
    
    # menu_options = ['''
    # 1. View video inventory
    # 2. View customer's rented videos
    # 3. Rent videos
    # 4. Return videos
    # 5. Add new customer
    # 6. Exit
    # ''']

    def __init__(self):                
        self.inventory = Inventory()
        self.customers = Customers()

    def run(self): # skeleton of choices available in welcome menu
        while True:
            self.print_menu()
            choice = self.get_user_menu_choice()
            print("")

            if choice == 1:
                self.inventory.print_inventory()
            elif choice == 2:
                self.customers.assign_rental_to_customer()
            elif choice == 3:
                self.inventory.rent_out_movies()
            elif choice == 4:
                self.inventory.return_movies()
            elif choice == 5:
                self.add_new_customer()
            elif choice == 6:
                break 
            
            print("")

    # welcome menu
    def print_menu(self):
        print("*******************************")
        print("Welcome to Code Platoon Video!")
        for option in self.menu_options:
            print(option)
        print("*******************************")


   # promts user to make desired selections:
    def get_user_menu_choice(self):
        num_choices = len(self.menu_options)
        if num_choices == 0:
            return 0

        choice = 0
        while choice == 0 or choice > num_choices: 
            choice = int(input(f"Please select 1-{num_choices}: "))
        return choice
   
        
        
        
        
    # @classmethod # pulls all customer data from database.
    # def get_all_customers_from_db(cls):
    #     with open(customer_path) as customers_file:
    #         customer = csv.DictReader(customers_file)
    #         for customer in customers:
    #             customers_list.append(customer["id"], customer["first_name"], customer["last_name"])
    #     return customers_list

