"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """

    def oddEvenList(self, head):
        # write your code here
        odds_head = odds = ListNode(0)
        evens_head = evens = ListNode(0)
        is_odd = True

        while head:
            if is_odd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            is_odd = not is_odd
            head = head.next

        evens.next = None
        odds.next = evens_head.next
        return odds_head.next
