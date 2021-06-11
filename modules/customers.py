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
        customer_id = Customers.get_all_customers()
        for value in customer_id:
            for customer in self.customers:
                if int(customer.id) == int(value["customer_id"]):
                    for rental in self.current_video_rentals:
                        print(f"rental: {rental}")
                        if rental.id == int(value["rental_id"]):
                            customer.rental = rental
                            print(f"customer rental(s): {customer.rental.first_name} {customer.rental.last_name}")    
        
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

