import unittest
from project8 import ConvertBin2Hex

class BinaryToHexConverterTest(unittest.TestCase):

    def setUp(self):
        self.single_converter = ConvertBin2Hex("1001")
        self.string_converter = ConvertBin2Hex("1010 1111")
        self.letter_converter = ConvertBin2Hex("1111")

    

    def test_single_digit(self):
        # Test a single hex value between 0 and 9
        expected_hex_value = '9'
        result_hex_value = self.single_converter.hexValue
        self.assertEqual(result_hex_value, expected_hex_value, "Conversion failed for a single digit.")
    
    def test_single_letter(self):
        # Test a single hex value between A and F
        expected_hex_value = 'F'
        result_hex_value = self.letter_converter.hexValue
        self.assertEqual(result_hex_value, expected_hex_value, "Conversion failed for a single letter.")
    
    def test_double_digit(self):
        # Test a case with two hex values
        expected_hex_value = 'AF'
        result_hex_value = self.string_converter.hexValue
        self.assertEqual(result_hex_value, expected_hex_value, "Conversion failed for two hex values.")

if __name__ == '__main__':
    unittest.main()
