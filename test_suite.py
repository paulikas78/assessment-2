import unittest
from modules.customer import Customer
from modules.video import Video

""" Tests for proper implementation of Customers class. """
class TestCustomers(unittest.TestCase):
    
    def setUp(self):
        self.test_customer = Customer(4,"Joe", "Cool", "Inception")
    
    def test_customer_lookup(self):
        self.assertTrue(self.test_customer.get_customer_id(), 4)
        
        
        
""" Tests for proper functioning of Inventory class and instances. """
class TestInventory(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        
    """ information is set up / torn down and tested, accordingly. """
    def setUp(self):
        self.test_customer = Customer(4,"Joe", "Cool", "Inception")
        self.test_rentals = Video(9, "Inception", "PG-13", 2)
        self.copies_to_rent = 1

    def tearDown(self):
        del self.test_rentals

    def test_initial_copies_available_for_rent(self):
        self.assertEqual(self.test_rentals.get_copies_available(), 2)

    def test_title(self):
        self.assertEqual(self.test_rentals.get_title(), "Inception")
        

if __name__ == "__main__":
    unittest.main()