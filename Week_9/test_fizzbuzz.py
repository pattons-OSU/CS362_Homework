#! python 3

"""
Simeon Patton
CS362 - Oregon State Spring 2021
Homework 7 - Question 1.1 
Test_fizzbuzz.py
"""

import unittest
import fizzbuzz

class testCaseVolume(unittest.TestCase):
    
    ## this test should pass, as the output is intended to be in a
    ## concantinated string format
    def test_datatype(self):
        self.assertTrue(type(fizzbuzz.output) == str)
    
    ##Test to see if program is executing based on user input
    def test_did_run(self):
        self.assertEqual(fizzbuzz.user_input(), 'y')


if __name__ == '__main__':
    unittest.main()