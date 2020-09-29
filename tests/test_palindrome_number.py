import unittest

if __name__ != '__main__':
    from leetcode.palindrome_number import Solution


class TestSolution(unittest.TestCase):
    def test_is_palindrome_1(self):
        """
        Input: 121
        Output: true
        """
        x = 121
        expected = True

        sol = Solution()
        result = sol.isPalindrome(x)

        self.assertEqual(result, expected)

    def test_is_palindrome_2(self):
        """
        Input: -121
        Output: false
        """
        x = -121
        expected = False

        sol = Solution()
        result = sol.isPalindrome(x)

        self.assertEqual(result, expected)

    def test_is_palindrome_3(self):
        """
        Input: 10
        Output: false
        """
        x = 10
        expected = False

        sol = Solution()
        result = sol.isPalindrome(x)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
    from leetcode.palindrome_number import Solution

    unittest.main()
