"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        def children_count(root):
            if root is None: return 0
            return 1 + children_count(root.left) + children_count(root.right)

        cnt = children_count(root.left)
        if k <= cnt: return self.kthSmallest(root.left, k)
        if k > cnt + 1: return self.kthSmallest(root.right, k - cnt - 1)
        return root.val
