"""
234. Palindrome Linked List
Easy


Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        last = slow.next
        while last.next:
            cur = last.next
            last.next = cur.next
            cur.next = slow.next
            slow.next = cur

        pre = head
        while slow.next:
            slow = slow.next
            if pre.val != slow.val:
                return False
            pre = pre.next

        return True
