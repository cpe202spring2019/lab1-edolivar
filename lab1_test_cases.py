import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)  
        tlist = [3,4,10,5,4,2]
        self.assertEqual(max_list_iter(tlist), 10) 

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,3,4,5,6]),[6,5,4,3,2,1])
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )
        self.assertEqual(bin_search(3, low, high, list_val), 3)
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)
        list_val = None
        low = 0
        high = 6
        with self.assertRaises(ValueError):
            bin_search(4, low, high, list_val)

if __name__ == "__main__":
        unittest.main()

    
