"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """

    def reorderList(self, head):
        # write your code here
        if not head or not head.next: return

        # find mid
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        # reverse the half after mid
        pre_mid, pre_cur = p1, p1.next
        while pre_cur.next:
            cur = pre_cur.next
            pre_cur.next = cur.next
            cur.next = pre_mid.next
            pre_mid.next = cur

        # reorder
        p1, p2 = head, pre_mid.next
        while p1 != pre_mid:
            pre_mid.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = pre_mid.next

        return
