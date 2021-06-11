import unittest
from modules.customers import Customers
from modules.rentals import Rentals
from modules.inventory import Inventory


class TestCustomers(unittest.TestCase):
    
    def test_customer_lookup(self):
        self.assertTrue(find_customer_with_id(1) == "John", "Young")

class TestRentals(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self):
        self.test_rentals = Rentals("Inception", 2)
        self.copies_to_rent = 1

    def tearDown(self):
        del self.test_rentals

    def test_initial_copies_available_for_rent(self):
        self.assertEqual(self.test_rentals.get_copies_available(), 2)

    def test_rental(self):
        new_copies_available_for_rent = self.test_rentals.rent_out_movies(self.copies_to_rent)
        self.assertEqual(new_copies_available_for_rent, 1)

class TestInventory(unittest.TestCase):
    def test_inventory(self):
    # pass
        
if __name__ == "__main__":
    unittest.main()