"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param A: An integer array
    @param queries: An query list
    @return: The result list
    """

    def intervalMinNumber(self, A, queries):
        # write your code here
        root = SegmentTree.build(0, len(A) - 1, A)
        return [SegmentTree.query(root, query.start, query.end)
                for query in queries]


class SegmentTree:
    def __init__(self, start, end, minimal=0):
        self.start = start
        self.end = end
        self.minimal = minimal
        self.left = None
        self.right = None

    @classmethod
    def build(cls, start, end, l):
        if start > end: return None
        if start == end: return SegmentTree(start, end, l[start])

        mid = (start + end) // 2
        node = SegmentTree(start, end, l[start])
        node.left = cls.build(start, mid, l)
        node.right = cls.build(mid + 1, end, l)
        node.minimal = min(node.left.minimal, node.right.minimal)
        return node

    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start: return float('inf')
        if start <= root.start and root.end <= end: return root.minimal
        return min(cls.query(root.left, start, end),
                   cls.query(root.right, start, end))
