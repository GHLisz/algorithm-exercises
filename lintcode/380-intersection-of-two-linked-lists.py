"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here
        if (not headA) or (not headB):
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a