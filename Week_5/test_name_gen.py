#! python3

import name_gen
import unittest

##Universal variables
first_name = name_gen.first_name_input()
last_name = name_gen.last_name_input()

class testCaseName(unittest.TestCase):
    
    ## Testing to make sure that type is string
    def test_type(self):
      self.assertTrue(type(first_name) is str)
      self.assertTrue(type(last_name) is str)

    ## Testing the output is correct with the concantination
    def test_expected_output(self):
        full_name = name_gen.full_name(first_name, last_name)
        self.assertEqual(full_name, name_gen.full_name(first_name, last_name))

    ##Testing to make sure that the string has actually been entered
    def test_length(self):
        full_name = name_gen.full_name(first_name, last_name)
        self.assertTrue(len(full_name) > 0)



if __name__ == '__main__':
    unittest.main()