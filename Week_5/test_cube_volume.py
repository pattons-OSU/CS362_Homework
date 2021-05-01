#! python3

import unittest
import cube_volume
import math


class testCaseVolume(unittest.TestCase):
    ## this test should pass, testing the actual arithmetic of the function
    def test_volume(self):
        self.assertEqual(cube_volume.cube_volume_calc(5), 125)

    ## testing a value error to see if the side length is negative
    def test_negative(self):
        negative_length = -4
        with self.assertRaises(ValueError) as exception_context:
            cube_volume.cube_volume_calc(negative_length)
        self.assertEqual(
            str(exception_context.exception),
            "A cube side length cannot be less than zero."
        )

    ## Testing to see if the input is a type value of "int"
    def test_type(self):
      self.assertTrue(cube_volume.user_input is int)

if __name__ == '__main__':
    unittest.main()