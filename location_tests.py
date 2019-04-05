import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_repr1(self):
        loc = Location("LA", 32.3, -13.7)
        self.assertEqual(repr(loc),"Location('LA', 32.3, -13.7)")
    
    def test_eq(self):
        loc1 = Location("LA", 32.3, -13.7)
        loc3 = loc1
        self.assertEqual((loc1 == loc3), True)
        loc1 = Location("LA", 32.3, -13.7)
        loc3 = Location("SLO", 35.3, -120.7)
        self.assertEqual((loc1 == loc3), False)
        loc1 = Location("LA", 32.3, -13.7)
        loc3 = Location("LA", 3.2, -13.7)
        self.assertEqual((loc1 == loc3), False)

    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
