import unittest

if __name__ != '__main__':
    from leetcode.reverse_integer import Solution


class TestSolution(unittest.TestCase):
    def test_reverse_1(self):
        """
        Input: 123
        Output: 321
        """
        x = 123

        expected = 321

        sol = Solution()
        result = sol.reverse(x)

        self.assertEqual(result, expected)

    def test_reverse_2(self):
        """
        Input: -123
        Output: -321
        """
        x = -123

        expected = -321

        sol = Solution()
        result = sol.reverse(x)

        self.assertEqual(result, expected)

    def test_reverse_3(self):
        """
        Input: 120
        Output: 21
        """
        x = 120

        expected = 21

        sol = Solution()
        result = sol.reverse(x)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
    from leetcode.reverse_integer import Solution

    unittest.main()
