"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """

    def sortedArrayToBST(self, A):
        # write your code here
        def convert(A, start, end):
            if start > end: return None
            if start == end: return TreeNode(A[start])

            mid = (start + end) // 2
            root = TreeNode(A[mid])
            root.left = convert(A, start, mid - 1)
            root.right = convert(A, mid + 1, end)
            return root

        return convert(A, 0, len(A) - 1)
