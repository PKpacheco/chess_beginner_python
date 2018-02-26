import unittest
from main import *

from unittest import mock


class TestChess(unittest.TestCase):

#     def test_input_ok_is_number(self):
#         with mock.patch('builtins.input', return_value=1):
#             self.assertEqual(get_num(), 1)

#     def test_input_fail_when_set_string(self):
#         with mock.patch('builtins.input', return_value='a'):
#             with self.assertRaises(ValueError):
#                 get_num()

#     def test_value_validation_out_of_range(self):
#         with self.assertRaises(RomanInvalidRange):
#             value_validation(4000)
#         with self.assertRaises(RomanInvalidRange):
#             value_validation(-1)        

#     def test_is_zero(self):
#         result = int_to_roman(0)
#         self.assertEqual(result, '')

#     def test_decimal_to_roman_units(self):
#         result = int_to_roman(1)
#         self.assertEqual(result, 'I')

#     def test_decimal_to_roman_dozens(self):
#         result = int_to_roman(11)
#         self.assertEqual(result, 'XI')

#     def test_decimal_to_roman_hundreds(self):
#         result = int_to_roman(111)
#         self.assertEqual(result, 'CXI')

#     def test_decimal_to_roman_thousands(self):
#         result = int_to_roman(1111)
#         self.assertEqual(result, 'MCXI')


# class TestRomanToInt(unittest.TestCase):
 
#     def test_input_is_letter(self):
#         with mock.patch('builtins.input', return_value='a'):
#             self.assertEqual(get_roman_letter(), 'a')

#     def test_input_fail_when_set_number(self):
#         with mock.patch('builtins.input', return_value=1):
#             with self.assertRaises(Exception):
#                 letter_validation()

#     def test_input_fail_when_set_invalid_roman(self):
#         with mock.patch('builtins.input', return_value='Z'):
#             with self.assertRaises(Exception):
#                 letter_validation()

#     def test_roman_to_decimal_unity(self):
#         result = roman_to_int("I")
#         self.assertEqual(result, 1)

#     def test_roman_to_decimal_dozens(self):
#         result = roman_to_int("XIV")
#         self.assertEqual(result, 14)

#     def test_roman_to_decimal_hundreds(self):
#         result = roman_to_int("CXX")
#         self.assertEqual(result, 120)

#     def test_roman_to_decimal_thousands(self):
#         result = roman_to_int("MMCX")
#         self.assertEqual(result, 2110)
if __name__ == "__main__":
    unittest.main()

