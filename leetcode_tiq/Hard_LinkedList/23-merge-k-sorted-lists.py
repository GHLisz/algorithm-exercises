"""
23. Merge k Sorted Lists
Hard


Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        def sol1():  # heap
            from heapq import heappush, heappop, heapreplace, heapify

            heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
            heapify(heap)
            dummy = cur = ListNode(0)

            while heap:
                val, i, node = heap[0]
                if not node.next:  # exhausted one linked-list
                    heappop(heap)
                else:
                    heapreplace(heap, (node.next.val, i, node.next))  # recycling tie-breaker i guarantees uniqueness
                cur.next = node
                cur = cur.next

            return dummy.next

        def sol2():
            def merge2(l1, l2):
                head = ListNode(-1)
                cur = head
                while l1 and l2:
                    if l1.val < l2.val:
                        cur.next = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                    cur = cur.next
                if l1:
                    cur.next = l1
                if l2:
                    cur.next = l2
                return head.next

            if not lists:
                return None

            n = len(lists)
            while n > 1:
                k = (n + 1) // 2
                for i in range(n // 2):
                    lists[i] = merge2(lists[i], lists[i + k])
                n = k
            return lists[0]

        return sol1()
