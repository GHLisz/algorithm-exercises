"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        helper = ListNode(0)
        helper.next = head

        cur = helper
        while cur.next and cur.next.next:
            tmp = cur.next.next
            cur.next.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next.next

        return helper.next
