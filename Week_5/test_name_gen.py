#! python3

import name_gen
import unittest

class testCaseName(unittest.TestCase):
    
    ## Testing to make sure that type is string
    def test_type(self):
      self.assertTrue(type(name_gen.first_name_input()) is str)
      self.assertTrue(type(name_gen.last_name_input()) is str)



if __name__ == '__main__':
    unittest.main()