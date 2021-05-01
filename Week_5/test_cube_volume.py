#! python3

import unittest
import cube_volume
from math import *


class testCaseVolume(unittest.TestCase):
    
##Testing pass and fail arithmetic    
    ## this test should pass, testing the actual arithmetic of the function
    def test_volume(self):
        self.assertEqual(cube_volume.cube_volume_calc(5), 125)
    ## This test should fail as the math is incorrect
    def test_volume_fail(self):
        self.assertEqual(cube_volume.cube_volume_calc(5), 25)

##Testing pass and fail negative entry
    ## testing a value error to see if the side length is negative
    def test_negative(self):
        negative_length = -4
        with self.assertRaises(ValueError) as exception_context:
            cube_volume.cube_volume_calc(negative_length)
        self.assertEqual(
            str(exception_context.exception),
            "A cube side length cannot be less than zero."
        )
    ##this test should fail as the side length given is a positive value
    def test_negative_fail(self):
        negative_length = 4
        with self.assertRaises(ValueError) as exception_context:
            cube_volume.cube_volume_calc(negative_length)
        self.assertEqual(
            str(exception_context.exception),
            "A cube side length cannot be less than zero."
        )        

##Testing pass and fail of the input type
    ## Testing to see if the input is a type value of "int"
    def test_type(self):
      self.assertTrue(type(cube_volume.user_input) is int)
    ## This test should fail as the input type IS int
    def test_type_fail(self):
      self.assertTrue(type(cube_volume.user_input) is not int)

if __name__ == '__main__':
    unittest.main()