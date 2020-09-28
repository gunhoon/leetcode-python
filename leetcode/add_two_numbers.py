# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
        """
        input1 = self.convertListToNumber(l1)
        input2 = self.convertListToNumber(l2)

        output = input1 + input2

        return self.convertNumberToList(output)

    def convertListToNumber(self, node: ListNode) -> int:
        """
        Input: (2 -> 4 -> 3)
        Output: 342
        """
        result = 0
        digit = 1

        while node is not None:
            result += node.val * digit
            node = node.next
            digit *= 10

        return result

    def convertNumberToList(self, num: int) -> ListNode:
        """
        Input: 342
        Output: (2 -> 4 -> 3)
        """
        digits = []
        if num == 0:
            digits.append(num)

        while num > 0:
            digits.insert(0, num % 10)
            num //= 10

        node = None
        for x in digits:
            node = ListNode(x, node)

        return node
