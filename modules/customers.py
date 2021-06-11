import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/customers.csv")

class Customers:
    
    def __init__(self, id, first_name, last_name, current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        
    @classmethod
    def get_all_customers(cls):
        with open(path) as customers_file:
            reader = csv.DictReader(customers_file)
            customers_list = []
            for row in reader:
                new_customer = Customers(int(row["id"]), row["first_name"], row["last_name"], row["current_video_rentals"])
                customers_list.append(new_customer)
        return customers_list
        
        
print(Customers.get_all_customers())

