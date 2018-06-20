"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """

    def plusOne(self, head):
        # Write your code here
        def reverse(head):  # destructive, modify existing nodes
            new_head = None
            while head:
                head.next, head, new_head = new_head, head.next, head
            return new_head

        p = h2 = reverse(head)
        while p:
            if p.val + 1 <= 9:
                p.val = p.val + 1
                break
            else:
                p.val = 0
                if not p.next:
                    p.next = ListNode(1)
                    break
                p = p.next
        return reverse(h2)
