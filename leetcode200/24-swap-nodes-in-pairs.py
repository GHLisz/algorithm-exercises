"""
24. Swap Nodes in Pairs
Medium


Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def sol1(head):  # recursive
            if not head or not head.next:
                return head

            node = head.next
            head.next = sol1(head.next.next)
            node.next = head
            return node

        def sol2(head):  # iterative
            dummy, dummy.next = ListNode(-1), head

            pre, pre.next = dummy, head
            while pre.next and pre.next.next:
                cur, nxt = pre.next, pre.next.next
                pre.next, nxt.next, cur.next = nxt, cur, nxt.next
                pre = cur
            return dummy.next

        return sol2(head)
