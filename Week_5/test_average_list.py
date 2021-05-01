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

if __name__ == '__main__':
    unittest.main()
    print(_list)