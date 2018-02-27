"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        # write your code here
        def merge(h1, h2):
            dummy = tail = ListNode(None)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next
            tail.next = h1 or h2
            return dummy.next

        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return merge(*map(self.sortList, (head, slow)))
