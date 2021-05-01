#! python3

## Simeon Patton
## CS362 HW4 Question 3.2
## April 30, 2021

## Write code that generates a full name when you provide the first and
## last name as inputs.

## Use the unittest module and write any 3 tests that can test out your
## code.

import name_gen
import unittest

##Universal variables
first_name = name_gen.first_name_input()
last_name = name_gen.last_name_input()

class testCaseName(unittest.TestCase):

##Testing true and false input type    
    ## Testing to make sure that type is string
    def test_type(self):
        self.assertTrue(type(first_name) is str)
        self.assertTrue(type(last_name) is str)
    ## This test will fail due to the wrong assertion
    def test_type_fail(self):
        self.assertFalse(type(first_name) is str)
        self.assertFalse(type(last_name) is str)

##Testing true and false string addition
    ## Testing the output is correct with the concantination
    def test_expected_output(self):
        full_name = name_gen.full_name(first_name, last_name)
        self.assertEqual(full_name, name_gen.full_name(first_name, last_name))
    ##This test will fail as last name is forced first
    def test_expected_output_fail(self):
        full_name = name_gen.full_name(last_name, first_name)
        self.assertEqual(full_name, name_gen.full_name(first_name, last_name))        

##Testing true and false entry of string
    ## Testing to make sure that the string has actually been entered
    def test_length(self):
        full_name = name_gen.full_name(first_name, last_name)
        self.assertTrue(len(full_name) > 0)
    ## Testing to make sure that nothing has been entered
    def test_length_fail(self):
        full_name = name_gen.full_name(first_name, last_name)
        self.assertTrue(len(full_name) == 0)


if __name__ == '__main__':
    unittest.main()