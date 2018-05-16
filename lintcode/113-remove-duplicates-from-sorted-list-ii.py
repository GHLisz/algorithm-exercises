"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head: return head

        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            head = self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)

        return head
