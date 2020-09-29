import unittest

if __name__ != '__main__':
    from leetcode.add_two_numbers import ListNode
    from leetcode.add_two_numbers import Solution
    from leetcode.add_two_numbers import FirstSolution


class TestSolution(unittest.TestCase):
    def test_add_two_numbers(self):
        """
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
        """
        l1 = ListNode(3, None)
        l1 = ListNode(4, l1)
        l1 = ListNode(2, l1)

        l2 = ListNode(4, None)
        l2 = ListNode(6, l2)
        l2 = ListNode(5, l2)

        expected = ListNode(8, None)
        expected = ListNode(0, expected)
        expected = ListNode(7, expected)

        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)

        # compare
        while expected is not None:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next

        self.assertEqual(result, expected)


class TestFirstSolution(unittest.TestCase):
    def test_add_two_numbers(self):
        """
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
        """
        l1 = ListNode(3, None)
        l1 = ListNode(4, l1)
        l1 = ListNode(2, l1)

        l2 = ListNode(4, None)
        l2 = ListNode(6, l2)
        l2 = ListNode(5, l2)

        expected = ListNode(8, None)
        expected = ListNode(0, expected)
        expected = ListNode(7, expected)

        sol = FirstSolution()
        result = sol.addTwoNumbers(l1, l2)

        # compare
        while expected is not None:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next

        self.assertEqual(result, expected)

    def test_convert_list_to_number(self):
        """
        Input: (2 -> 4 -> 3)
        Output: 342
        """
        l1 = ListNode(3, None)
        l1 = ListNode(4, l1)
        l1 = ListNode(2, l1)

        l2 = ListNode(4, None)
        l2 = ListNode(0, l2)
        l2 = ListNode(5, l2)

        l3 = ListNode(0, None)

        expected1 = 342
        expected2 = 405
        expected3 = 0

        sol = FirstSolution()

        result = sol.convertListToNumber(l1)
        self.assertEqual(result, expected1)

        result = sol.convertListToNumber(l2)
        self.assertEqual(result, expected2)

        result = sol.convertListToNumber(l3)
        self.assertEqual(result, expected3)

    def test_convert_number_to_list(self):
        """
        Input: 342
        Output: (2 -> 4 -> 3)
        """
        input1 = 342
        input2 = 8902
        input3 = 0

        expected1 = ListNode(3, None)
        expected1 = ListNode(4, expected1)
        expected1 = ListNode(2, expected1)

        expected2 = ListNode(8, None)
        expected2 = ListNode(9, expected2)
        expected2 = ListNode(0, expected2)
        expected2 = ListNode(2, expected2)

        expected3 = ListNode(0, None)

        sol = FirstSolution()

        # input 1
        result = sol.convertNumberToList(input1)
        expected = expected1
        while expected is not None:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next

        self.assertEqual(result, None)

        # input 2
        result = sol.convertNumberToList(input2)
        expected = expected2
        while expected is not None:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next

        self.assertEqual(result, None)

        # input 3
        result = sol.convertNumberToList(input3)
        expected = expected3
        while expected is not None:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next

        self.assertEqual(result, None)


if __name__ == '__main__':
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
    from leetcode.add_two_numbers import ListNode
    from leetcode.add_two_numbers import Solution
    from leetcode.add_two_numbers import FirstSolution

    unittest.main()
