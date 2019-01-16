"""
21. Merge Two Sorted Lists
Easy


Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def sol1(l1, l2):  # iteratively
            dummy = cur = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next

        def sol2(l1, l2):  # recursively
            if not all([l1, l2]):
                return l1 or l2
            if l1.val < l2.val:
                l1.next = sol2(l1.next, l2)
                return l1
            else:
                l2.next = sol2(l1, l2.next)
                return l2

        return sol1(l1, l2)
