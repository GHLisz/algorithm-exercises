"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: l1: The first list.
    @param: l2: The second list.
    @return: the sum list of l1 and l2.
    """

    def addLists2(self, l1, l2):
        # write your code here
        ans = None
        stack1, stack2 = [], []
        while l1 or l2:
            if l1:
                stack1.append(l1)
                l1 = l1.next
            if l2:
                stack2.append(l2)
                l2 = l2.next
        a, b, carry, sum_ = 0, 0, 0, 0
        while stack1 or stack2:
            a = stack1.pop().val if stack1 else 0
            b = stack2.pop().val if stack2 else 0
            sum_ = a + b + carry
            tmp = ListNode(sum_ % 10)
            tmp.next = ans
            ans = tmp
            carry = sum_ // 10
        if carry:
            tmp = ListNode(carry)
            tmp.next = ans
            ans = tmp

        return ans
