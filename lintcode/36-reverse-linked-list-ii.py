"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: ListNode head is the head of the linked list
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(0, head)
        pre = dummy  # make a pointer pre as a marker for the node before reversing

        for i in range(1, m):
            pre = pre.next

        start = pre.next  # a pointer to the beginning of a sub-list that will be reversed
        then = start.next  # a pointer to a node that will be reversed

        # 1 - 2 -3 - 4 - 5 ; m=2; n =4 ---> pre = 1, start = 2, then = 3

        for i in range(m, n):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next

        # first reversing : dummy->1 - 3 - 2 - 4 - 5; pre = 1, start = 2, then = 4
        # second reversing: dummy->1 - 4 - 3 - 2 - 5; pre = 1, start = 2, then = 5 (finish)

        return dummy.next
