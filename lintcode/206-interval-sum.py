"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """

    def intervalSum(self, A, queries):
        # write your code here
        class SegmentTreeNode:
            def __init__(self, start, end, sum):
                self.start = start
                self.end = end
                self.sum = sum
                self.left = None
                self.right = None

        def build(L, start, end):
            if start > end: return None
            root = SegmentTreeNode(start, end, 0)
            if start != end:
                mid = (start + end) // 2
                root.left = build(L, start, mid)
                root.right = build(L, mid + 1, end)
                root.sum = root.left.sum + root.right.sum
            else:
                root.sum = L[start]
            return root

        def query(root, start, end):
            if root.start == start and root.end == end:
                return root.sum
            mid = (root.start + root.end) // 2
            left_sum, right_sum = 0, 0
            if start <= mid:
                if mid < end:
                    left_sum = query(root.left, start, mid)
                else:
                    left_sum = query(root.left, start, end)
            if mid < end:
                if start <= mid:
                    right_sum = query(root.right, mid+1, end)
                else:
                    right_sum = query(root.right, start, end)
            return left_sum + right_sum

        root = build(A, 0, len(A)-1)
        return [query(root, q.start, q.end) for q in queries]
