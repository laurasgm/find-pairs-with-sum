import unittest
from sum_pairs import find_pairs_with_sum

class TestSumPairs(unittest.TestCase):
    def test_find_pairs_with_sum(self):
        # Test 1: Normal case with positive integers
        input_list = [1, 9, 5, 0, 20, -4, 12, 16, 7]
        target = 12
        expected_result = [(12, 0), (16, -4), (7, 5)]
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_result)

        # Test 2: All elements are zero
        input_list = [0, 0, 0, 0]
        target = 0
        expected_result = [(0, 0), (0, 0), (0, 0)]
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_result)

        # Test 3: No pairs that sum to the target
        input_list = [1, 2, 3, 4, 5]
        target = 10
        expected_result = []
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_result)

        # Test 4: Negative numbers
        input_list = [5, -3, -1, 7, -8, 4]
        target = 2
        expected_result = [(-3, 5)]
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_result)

if __name__ == '__main__':
    unittest.main()
