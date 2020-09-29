import unittest

if __name__ != '__main__':
    from leetcode.longest_substring_without_repeating_characters import Solution


class TestSolution(unittest.TestCase):
    def test_length_of_longest_substring_1(self):
        """
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        """
        s = 'abcabcbb'

        expected = 3

        sol = Solution()
        result = sol.lengthOfLongestSubstring(s)

        self.assertEqual(result, expected)

    def test_length_of_longest_substring_2(self):
        """
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        """
        s = 'bbbbb'

        expected = 1

        sol = Solution()
        result = sol.lengthOfLongestSubstring(s)

        self.assertEqual(result, expected)

    def test_length_of_longest_substring_3(self):
        """
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        """
        s = 'pwwkew'

        expected = 3

        sol = Solution()
        result = sol.lengthOfLongestSubstring(s)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
    from leetcode.longest_substring_without_repeating_characters import Solution

    unittest.main()
