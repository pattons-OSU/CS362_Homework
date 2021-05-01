#! python3

import average_list
import math
import unittest

class testCaseList(unittest.TestCase):
    
## Testing pass and fail for what we expect the list to be    
    ## This test should pass, making sure that the list is what we expect it to be
    def test_list_items(self):
        _list = average_list.user_list()
        expected = [9, 5, 6, 93]
        self.assertEqual(_list, expected)
    ##This test should fail as the list differs from what is expected
    def test_list_items_fail(self):
        _list = average_list.user_list()
        expected = [93, 53, 63, 9]
        self.assertEqual(_list, expected)

## Testing pass and fail to make sure that the list is not empty
    ## This test to make sure that the list is not empty
    def test_empty(self):
        self.assertTrue(average_list.user_list())
    ##now, testing to make sure that the list is populated, should FAIL
    def test_populated(self):
        self.assertFalse(average_list.user_list())

## testing pass and fail of the average function vs known amount    
    ## this test should pass as it is what is expected from the average function
    def test_average(self):
        number_list = average_list.user_list()
        calculated_average = average_list.average_of_list(number_list)
        expected_average = 28.25
        self.assertEqual(expected_average, calculated_average)
    ## this test should fail as the expected average is not correct
    def test_average_fail(self):
        number_list = average_list.user_list()
        calculated_average = average_list.average_of_list(number_list)
        expected_average = 93
        self.assertEqual(expected_average, calculated_average)
    

if __name__ == '__main__':
    unittest.main()