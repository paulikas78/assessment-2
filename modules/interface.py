from modules.customers import Customers
from modules.inventory import Inventory
from modules.rentals import Rentals

class Interface:    # creates interface for customers to use, regarding their respective accounts.

    menu_options = ["""
    1. View video inventory
    2. View customer's rented videos
    3. Rent videos
    4. Return videos
    5. Add new customer
    6. Exit
    """]

    def __init__(self):                
        self.inventory = Inventory()
        self.rentals = Rentals()
        self.customers = Customers()
        self.all_customers = []

    def run(self): # skeleton of choices available in welcome menu
        while True:
            self.print_menu()
            choice = self.get_user_menu_choice()
            print("")

            if choice == 1:
                self.view_video_inventory()
            elif choice == 2:
                self.view_customers_rented_videos()
            elif choice == 3:
                self.rent_videos()
            elif choice == 4:
                self.return_videos()
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

    def view_video_inventory(self):
        inventory = self.inventory.get_inventory()
        print(f"The current available videos are {inventory}")
        

    def view_customers_rented_videos(self):
        rentals = self.rentals.get_all_customer_rentals()
        print(f"Your currently rented videos are {rentals}")

    def rent_videos(self):
        title = int(input("Enter Title: "))
        copies = int(input("Enter copies to rent: "))
        rent = Rentals(title, copies)

        try:
            self.rentals.rent_out_movies(rent)
            print(f"Congratulations!!  You have rented your movie, '{title}'!!")
        except Exception as x:
            print(f"ERROR: {x}")

    def return_videos(self):
        title = int(input("Enter Title: "))
        copies = int(input("Enter copies to rent: "))
        self.rentals.return_movies(title, copies)
        
    def add_new_customer(self):  # allows new customers to register and assigns new customer id.
        first_name = input("Enter new customer's first name: ")
        last_name = input("Enter new customer's last name: ")
        all_customers = Interface.get_all_customers_from_db()
        id = len(all_customers) + 1
        print(f"Thanks you, {first_name} {last_name}, for becoming a new customer!!  Your customer id is {id}")
        self.save_customers(all_customers)
        
    def save_customers(self, all_customers): # saves new customer data
        with open(customer_path, "w") as csvfile:
            customer_csv = csv.writer(csvfile, delimiter = ",")
            customer_csv.writerow(["id", "first_name", "last_name"])
            for customer in all_customers:
                customer_csv.writerow([customer.first_name, customer.last_name])
        
        
    @classmethod # pulls all customer data from database.
    def get_all_customers_from_db(cls):
        with open(customer_path) as customers_file:
            customer = csv.DictReader(customers_file)
            customers_list = []
            for customer in customers:
                customers_list.append(customer["id"], customer["first_name"], customer["last_name"])
        return customers_list

