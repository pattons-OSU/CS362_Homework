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

if __name__ == '__main__':
    unittest.main()