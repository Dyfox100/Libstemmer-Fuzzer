import unittest

from string_fuzzer import String_Fuzzer


class Test_String_Fuzzer(unittest.TestCase):
    def setUp(self):
        self.string_fuzzer = String_Fuzzer(mock_testing_strategy)

    def test_string_fuzzer_follows_strategy_provided(self):
        result = self.string_fuzzer.generate_fuzzy_string(2)
        self.assertEqual(result, b"aa")

    def test_string_fuzzer_returns_correct_length_string(self):
        result = self.string_fuzzer.generate_fuzzy_string(5)
        self.assertEqual(len(result), 5)


def mock_testing_strategy():
    return b"a"

if __name__ == "__main__":
    unittest.main()
