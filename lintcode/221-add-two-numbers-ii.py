"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """

    def addLists2(self, l1, l2):
        # write your code here
        ans, stk1, stk2 = None, [], []
        for l, stk in (l1, stk1), (l2, stk2):
            while l:
                stk.append(l)
                l = l.next

        a, b, carry, total = 0, 0, 0, 0
        while stk1 or stk2:
            a = stk1.pop().val if stk1 else 0
            b = stk2.pop().val if stk2 else 0
            total = a + b + carry
            tmp = ListNode(total % 10)
            tmp.next = ans
            ans = tmp
            carry = total // 10
        if carry:
            tmp = ListNode(carry)
            tmp.next = ans
            ans = tmp
        return ans
