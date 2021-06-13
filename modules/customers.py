import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/customers.csv")

class Customers:
    customers_list = []
    
    def __init__(self):
        # self.customers = Customers()
        pass
        
    def assign_rental_to_customer(self):    # assigns video rental to customer
        self.get_all_customers_rentals()
        for row in self.customers_list:
            print(f"id: {row['id']}, first name: {row['first_name']}, last name: {row['last_name']}, current video rentals: {row['current_video_rentals']}")
            
    def add_new_customer(self):  # allows new customers to register and assigns new customer id.
        self.get_all_customers_rentals()
        first_name = input("Enter new customer's first name: ")
        last_name = input("Enter new customer's last name: ")
        id = int(len(customers_list) + 1)
        # all_customers = self.customers.get_all_customers_from_db()
        print(f"Thank you, {first_name} {last_name}, for becoming a new customer!!  Your customer id is {id}")
        self.save_customers(all_customers)
        
    def save_customers(self): # saves new customer data
        self.get_all_customers_rentals()
        with open(customer_path, "w") as csvfile:
            customer_csv = csv.writer(csvfile, delimiter = ",")
            customer_csv.writerows(['id', 'first_name', 'last_name'])
            for customer in customers_list:
                customer_csv.writerows([customer.id, customer.first_name, customer.last_name])        
    
        
    # @classmethod   # acquires customer data -- move elsewhere
    def get_all_customers_rentals():
        with open(path) as customers_file:
            reader = csv.DictReader(customers_file)
            for row in reader:
                new_customer = self.customers(int(row['id']), row['first_name'], row['last_name'], row['current_video_rentals'])
                customers_list.append(new_customer)
        return customers_list
    
    # def to_string(self):
    #     return self.id + "," + self.first_name + "," + self.last_name,self.current_video_rentals # output to csv file
        
        


