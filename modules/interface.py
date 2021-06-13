import csv
from modules import customer, video
import modules
import os
import sys
sys.path.append('/Users/codeplatoon/assessment-2/modules')
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

inventory_path = '/Users/codeplatoon/assessment-2/data/inventory.csv'
customer_path = '/Users/codeplatoon/assessment-2/data/customers.csv'
video_fieldnames = ['id','title','rating','copies_available']
customer_fieldnames = ['id','first_name','last_name','current_video_rentals']
from modules.customer import Customer
from modules.video import Video

class Interface:    # creates interface for customers to use, regarding their respective accounts.

    menu_options = ['\n1. View video inventory', '\n2. View customer\'s rented videos', '\n3. Rent videos', '\n4. Return videos', '\n5. Add new customer', '\n6. Exit']
    

    def __init__(self):                
        
        self.customer_list = []
        self.vid_list = []
        self.customer_db = []
        self.inventory_db = []
        
        

    def run(self): # skeleton of choices available in welcome menu
        
        # Read Customers file
        with open(customer_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                print(row)
                self.customer_db.append(row)
                rentals = row['current_video_rentals']
                list = rentals.split('/')
                c = Customer(row['id'], row['first_name'], row['last_name'], list)
                self.customer_list.append(c)
                
        # Read Videos file
        with open(inventory_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                self.inventory_db.append(row)
                v = Video(row['id'], row['title'], row['rating'], row['copies_available'])
                self.vid_list.append(v)
        
        while True:
            self.print_menu()
            choice = self.get_user_menu_choice()
            print("")

            if choice == 1:
                for video in self.vid_list:
                    video.print_video()
            elif choice == 2:
                id = input("Enter the customer you would like to see rentals for: ")
                cust = self.get_customer_by_id(int(id))
                if cust.rental_list is None:
                    print("Customer has no rentals!")
                    continue
                print(cust.get_rental_list())
            elif choice == 3:
                title = input("Enter the movie title ")
                id = input("Enter the customer ID renting this movie ")
                
                cust = self.get_customer_by_id(int(id))
            
                if self.check_inventory(title):
                    cust.assign_rental_to_customer(title)
                    self.write_inventory(title, id)
            elif choice == 4:
                title = input("Enter the movie title ")
                id = input("Enter the customer ID returning this movie ")
                
                cust = self.get_customer_by_id(int(id))
                cust.return_rental_from_customer(title)
                self.write_return_inventory(title, id)
                
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
   
        
    # confirm a copy of requested movie exists in inventory   
    def check_inventory(self, title):
        with open(inventory_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                if row['title'] == title and int(row['copies_available']) > 0:
                    return True
            print('Movie is unavailable to rent!')
            return False

    def add_new_customer(self):  # allows new customers to register and assigns new customer id.
        first_name = input("Enter new customer's first name: ")
        last_name = input("Enter new customer's last name: ")
        id = int(len(self.customer_list) + 1)
        current_rentals = ''
        
        new_cust = Customer(id, first_name, last_name, [current_rentals])
        self.customer_list.append(new_cust)
        
        entry = {'id': id, 'first_name': first_name, 'last_name':last_name, 'current_video_rentals':current_rentals}
        self.customer_db.append(entry)
   
        print(f"Thank you, {first_name} {last_name}, for becoming a new customer!!  Your customer id is {id}")
        with open(customer_path, 'a+') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter = ",")
            customer_csv.writerow([id, first_name, last_name, current_rentals])            
   
    def get_customer_by_id(self, id) -> Customer:
        for customer in self.customer_list:
            if int(customer.get_customer_id()) == id:
                return customer
    
    # Method to update csv files when renting a video
    def write_inventory(self, title, cust_id):
        
        # customers.csv update
        entry = self.customer_db[int(cust_id) - 1]
        print(entry)
        string = '/' + title
        entry['current_video_rentals'] += string
        with open(customer_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=customer_fieldnames)
            writer.writeheader()
            for line in self.customer_db:
                writer.writerow(line)
        
        # inventory.csv update
        for dict in self.inventory_db:
            if dict['title'] == title:
                num_copies = int(dict['copies_available'])
                num_copies -= 1
                dict['copies_available'] = num_copies
        with open(inventory_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=video_fieldnames)
            writer.writeheader()
            for line in self.inventory_db:
                writer.writerow(line)
    
    # method to update csv files when returning a video
    def write_return_inventory(self, title, cust_id):
       
        # customer.csv update 
        entry = self.customer_db[int(cust_id) - 1]
        print(entry)
        list = entry['current_video_rentals'].split('/')
        list.remove(title)
        temp = ''
        for item in list:
            string = item + '/'
            temp += string
        entry['current_video_rentals'] = temp
        with open(customer_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=customer_fieldnames)
            writer.writeheader()
            for line in self.customer_db:
                writer.writerow(line)
        
        # inventory.csv update
        for dict in self.inventory_db:
            if dict['title'] == title:
                num_copies = int(dict['copies_available'])
                num_copies += 1
                dict['copies_available'] = num_copies
        with open(inventory_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=video_fieldnames)
            writer.writeheader()
            for line in self.inventory_db:
                writer.writerow(line)
     