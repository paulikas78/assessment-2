import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

from modules.customers import Customers

class Inventory:
    movie_title = []
    
    
    def __init__(self):
        # self.name = name
        # self.customers = Customers()
        # self.inventory = Inventory()
        pass
        
    def print_inventory(self): # prints inventory of all videos.
        i_list = self.get_inventory()
        for row in i_list:
            print(f"movie id: {row['id']}, title: {row['title']}, rating: {row['rating']}, copies available: {row['copies_available']}")     
            
    def rent_out_movies(self): 
        self.get_inventory()
        # input if / counter not allowing more than 3 rentals
        rented_movie_title = input("Enter movie title you'd like to rent: ")
        for movie_title in self.inventory_list:
            if movie_title["title"] == rented_movie_title:
                self.movie_title.append(movie_title["title"])
                new_copies_available = int(movie_title["copies_available"])
                new_copies_available -= 1
            # elif -- movie title isn't available
            
        def return_movies(self):
            self.get_inventory()
            rented_movie_title = input("Enter movie title you'd like to return: ")
            for movie_title in self.inventory_list:
                if movie_title["title"] == rented_movie_title:
                    self.movie_title.append(movie_title["title"])
                    new_copies_available = int(movie_title["copies_available"])
                    new_copies_available += 1
                            
    @classmethod # searches inventory
    def get_inventory(cls):
        with open(path) as inventory_file:
            reader = csv.DictReader(inventory_file)
            inventory_list = []
            for row in reader:
                new_inventory = dict(row)
                inventory_list.append(new_inventory)
        return inventory_list
    