import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")

class Video:
    
    def __init__(self, video_id, video_title, rating, num_copies):
        
        self.video_id = video_id
        self.video_title = video_title
        self.rating = rating
        self.num_copies = num_copies
        
    def print_video(self): # print information about video
        print(f"video id: {self.video_id}, title: {self.video_title}, rating: {self.rating}, copies available: {self.num_copies}")
        
    def get_copies_available(self):
        return self.num_copies
    
    def get_title(self):
        return self.video_title