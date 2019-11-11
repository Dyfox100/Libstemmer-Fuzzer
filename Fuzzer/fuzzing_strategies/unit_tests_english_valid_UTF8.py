import unittest

from english_valid_UTF8_strategy import English_Valid_UTF8_Strategy

class Test_English_UTF8_Strategy(unittest.TestCase):
    def setUp(self):
        self.strategy = English_Valid_UTF8_Strategy()

    def test_english_utf8_strat_returns_valid_char_less_than_255(self):
        for __ in range(100):
            result = self.strategy.generate()
            #ensure valid utf8
            str(result, 'utf-8')
            #ensure standard english ascii
            self.assertLessEqual(ord(result), 255)

if __name__ == "__main__":
    unittest.main()
