import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

from .customers import Customers

class Rentals:
    maximum_rentals = 3
    
      def __init__(self,id,title,rating,copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available
        
    def rent_out_movie(self, copies):
        new_copies_available = self.copies_available - copies
        if copies > maximum_rentals:
            print(f"YOU CAN ONLY HAVE {maximum_rentals} videos rented at once.")
        elif new_copies_available > self.copies_available:
            print(f"Sorry.  There are {self.copies_available} copies available of this title.")
        else:
            self.copies_available = new_copies_available
            
    def return_movie(self, copies):
        self.copies_available += copies

    def get_copies_available(self):
        return self.copies_available
    
    @classmethod
    def get_all_customer_rentals(cls):
        with open(path) as customer_rentals_file:
            reader = csv.DictReader(customer_rentals_file)
            customer_rentals_list = []
            for row in reader:
                new_customer_rentals = Rentals(int(row["id"]), int(row["title"]), row["rating"], row["copies_available"])
                customer_rentals_list.append(new_customer_rentals)
        return customer_rentals_list
    