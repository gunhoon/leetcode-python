import unittest

if __name__ != '__main__':
    from leetcode.two_sum import Solution


class TestSolution(unittest.TestCase):
    def test_two_sum_1(self):
        """
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        nums = [2,7,11,15]
        target = 9

        expected = [0,1]

        sol = Solution()
        result = sol.twoSum(nums, target)

        self.assertEqual(result, expected)

    def test_two_sum_2(self):
        """
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        """
        nums = [3,2,4]
        target = 6

        expected = [1,2]

        sol = Solution()
        result = sol.twoSum(nums, target)

        self.assertEqual(result, expected)

    def test_two_sum_3(self):
        """
        Input: nums = [3,3], target = 6
        Output: [0,1]
        """
        nums = [3,3]
        target = 6

        expected = [0,1]

        sol = Solution()
        result = sol.twoSum(nums, target)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
    from leetcode.two_sum import Solution

    unittest.main()
