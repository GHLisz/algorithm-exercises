"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """

    def isPalindrome(self, head):
        # write your code here
        if not head or not head.next: return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        last, pre = slow.next, head
        while last.next:
            tmp = last.next
            last.next = tmp.next
            tmp.next = slow.next
            slow.next = tmp

        while slow.next:
            slow = slow.next
            if pre.val != slow.val:
                return False
            pre = pre.next

        return True
