"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        def b(A, start, end):
            if start > end:
                return None
            if start == end:
                node = SegmentTreeNode(start, end)
                node.max = A[start]
                return node
            node = SegmentTreeNode(start, end)
            node.left = b(A, start, (start+end)/2)
            node.right = b(A, (start+end)/2+1, end)
            node.max = max(node.left.max, node.right.max)
            return node

        return b(A, 0, len(A)-1)
