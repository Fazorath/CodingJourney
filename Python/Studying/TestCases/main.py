import unittest
from project8 import ConvertBin2Hex

class BinaryToHexConverterTest(unittest.TestCase):

    def setUp(self):
        # Instantiate the ConvertBin2Hex class here with valid arguments
        self.single_converter = ConvertBin2Hex("1001")
        
    

    def test_single_digit(self):
        # Test a single hex value between 0 and 9
        binary = "1001"
        expected_hex_value = '9'
        result_hex_value = self.single_converter.hexValue
        self.assertEqual(result_hex_value, expected_hex_value, "Conversion failed for a single digit.")


if __name__ == '__main__':
    unittest.main()
