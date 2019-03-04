"""
148. Sort List
Medium


Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def get_size(head):
            c = 0
            while head:
                c += 1
                head = head.next
            return c

        def split(head, step):
            i = 1
            while head and i < step:
                head = head.next
                i += 1
            if not head:
                return None
            tmp, head.next = head.next, None
            return tmp

        def merge(l, r, head):
            cur = head
            while l and r:
                if l.val < r.val:
                    cur.next, l = l, l.next
                else:
                    cur.next, r = r, r.next
                cur = cur.next
            cur.next = l or r
            while cur.next:
                cur = cur.next
            return cur

        size, step = get_size(head), 1
        dummy = ListNode(0)
        dummy.next = head

        while step < size:
            cur, tail = dummy.next, dummy
            while cur:
                l = cur
                r = split(l, step)
                cur = split(r, step)
                tail = merge(l, r, tail)
            step *= 2
        return dummy.next
