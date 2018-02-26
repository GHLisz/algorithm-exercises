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
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return head
        l_head, r_head = ListNode(0), ListNode(0)
        l_tail, r_tail = l_head, r_head
        while head is not None:
            if head.val < x:
                l_tail.next = head
                l_tail = l_tail.next
            else:
                r_tail.next = head
                r_tail = r_tail.next
            head = head.next
        r_tail.next = None
        l_tail.next = r_head.next
        return l_head.next
