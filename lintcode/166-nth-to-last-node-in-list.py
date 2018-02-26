"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        # write your code here
        if head is None or n < 1:
            return None

        fast = slow = head

        for i in range(0, n):
            fast = fast.next

        while fast is not None:
            fast, slow = fast.next, slow.next

        return slow
