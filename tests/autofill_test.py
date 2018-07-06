__author__ = 'Nhat Nguyen, Minh Phuong'
#imports unittest 
import unittest
from src.autofill import Columns
col = Columns
#testing class that tests all four functions in the Calculate file
class AutofillTester(unittest.TestCase):

    def test_autofill_in_array(self):
        # col.array1 = []
        # col.array2 = []
        # self.assertEqual(col.autofill_data(af), [])
        pass

#calls the unittest's main method
if __name__ == '__main__':
    unittest.main()