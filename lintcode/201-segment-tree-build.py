"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""

class Solution:
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        if start > end: return None
        if start == end: return SegmentTreeNode(start, end)
        root = SegmentTreeNode(start, end)
        root.left = self.build(start, (start+end)/2)
        root.right = self.build((start+end)/2+1, end)
        return root
