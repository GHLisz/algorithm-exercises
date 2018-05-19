"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        # write your code here
        if not head: return None

        n, cur = 1, head
        while cur.next:
            n += 1
            cur = cur.next

        cur.next = head
        m = n - k % n
        for _ in range(m):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        return new_head
