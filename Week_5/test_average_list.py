#! python3

import average_list
import math
import unittest

class testCaseVolume(unittest.TestCase):
    
    ## This test should pass, making sure that the list is what we expect it to be
    def test_list_items(self):
        _list = average_list.user_list()
        expected = [9, 5, 6, 93]
        self.assertEqual(_list, expected)

    ## This test to make sure that the list is not empty
    def test_empty(self):
        self.assertTrue(average_list.user_list())
    ##now, testing to make sure that the list is populated, should FAIL
    def test_populated(self):
        self.assertFalse(average_list.user_list())

    
    ## Testing average function
    def test_average(self):
        number_list = average_list.user_list()
        calculated_average = average_list.average_of_list(number_list)
        expected_average = 28.25
        self.assertEqual(expected_average, calculated_average)

    

if __name__ == '__main__':
    unittest.main()