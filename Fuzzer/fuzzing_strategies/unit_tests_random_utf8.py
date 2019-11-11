import unittest

from random_non_valid_utf8 import Random_Non_Valid_UTF8_Strategy

class Test_Random_Nonvalid_UTF8(unittest.TestCase):
    def setUp(self):
        self._strategy = Random_Nonvalid_UTF8_Strategy()

    def test_random_nonvalid_utf8_return_values_change_on_multiple_runs(self):
        result1 = self._strategy.generate()
        result2 = self._strategy.generate()

        if result1 == result2:
            #try again,
            #very low probability that they are randomly selected
            #to be exactly the same. Fail test if happens twice.
            result1 = self._strategy.generate()
            result2 = self._strategy.generate()

        self.assertNotEqual(result1, result2)

    def test_random_nonvalid_utf8_returns_length_4_or_less_byte_strings(self):
        for __ in range(100):
            result1 = self._strategy.generate()
            result2 = self._strategy.generate()
            self.assertLessEqual(len(result1), 4)
            self.assertLessEqual(len(result2), 4)

    def test_random_nonvalid_utf8_returns_valid_hex_encoded_values(self):
        result = self._strategy.generate()
        #should succeed without throwing vlaue error
        int(result.hex(), 16)

if __name__ == "__main__":
    unittest.main()
