#! python 3

"""
Simeon Patton
CS362 - Oregon State Spring 2021
Homework 7 - Question 2.1
test_leapyear.py
"""

import unittest
import leapyear

class testCaseVolume(unittest.TestCase):
    
    ## this test should pass, as the user input is intended to be
    ## an integer and not a string
    def test_datatype(self):
        self.assertTrue(type(leapyear.user_input()) == int)
    
    
if __name__ == '__main__':
    unittest.main()
