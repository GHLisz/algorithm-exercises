"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        # write your code here
        if v1 == v2: return head

        pre_v1, cur_v1 = None, head
        while cur_v1 and cur_v1.val != v1:
            pre_v1, cur_v1 = cur_v1, cur_v1.next

        pre_v2, cur_v2 = None, head
        while cur_v2 and cur_v2.val != v2:
            pre_v2, cur_v2 = cur_v2, cur_v2.next

        if not all([cur_v1, cur_v2]): return head

        if pre_v1 is not None:
            pre_v1.next = cur_v2
        else:
            head = cur_v2

        if pre_v2 is not None:
            pre_v2.next = cur_v1
        else:
            head = cur_v1

        cur_v1.next, cur_v2.next = cur_v2.next, cur_v1.next

        return head
