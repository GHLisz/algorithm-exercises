"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        def sol1():
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

            if not lists: return None
            n = len(lists)
            while n > 1:
                k = (n + 1) // 2
                for i in range(n // 2):
                    lists[i] = merge2(lists[i], lists[i + k])
                n = k
            return lists[0]

        def sol2():
            import heapq

            def heappush_node(heap, node):
                heapq.heappush(heap, (node.val, node))

            if not lists: return None
            trav = dummy = ListNode(-1)
            heap = []
            for l1 in lists:
                if l1:
                    heappush_node(heap, l1)
            while heap:
                node = heapq.heappop(heap)[1]
                trav.next = node
                trav = trav.next
                if trav.next:
                    heappush_node(heap, trav.next)

            return dummy.next

        return sol1()
