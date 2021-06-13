import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/customers.csv")
class Customer:
    
   
    
    def __init__(self, customer_id, first_name, last_name, rental_list):
        
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.rental_list = rental_list
     
    
    def print_customer(self):
        print(f"customer id: {self.customer_id}, first name: {self.first_name}, last name: {self.last_name}, rental list: {self.rental_list}")
        
    def get_customer_id(self):
        return self.customer_id
    
    def get_rental_list(self):
        return self.rental_list
    
      # assigns video rental to customer    
    def assign_rental_to_customer(self, title):    
        if (len(self.rental_list) == 3):
            print('Customer has reached rental limit!\n')
        else:
            self.rental_list.append(title)
                             
    def return_rental_from_customer(self, title):
        try:
            self.rental_list.remove(title) 
        except:
            print('Customer does not have this currently rented')  
