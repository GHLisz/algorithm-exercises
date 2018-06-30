"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        def find(res, root, cur_sum, target, paths):
            cur_sum += root.val
            paths.append(root.val)
            if cur_sum == target and not any([root.left, root.right]):
                res.append(paths[:])
            else:
                if root.left: find(res, root.left, cur_sum, target, paths)
                if root.right: find(res, root.right, cur_sum, target, paths)
            paths.pop()

        if not root: return []
        res = []
        find(res, root, 0, target, [])
        return res
