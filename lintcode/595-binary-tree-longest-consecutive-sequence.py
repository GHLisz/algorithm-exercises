"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        # write your code here
        def dfs(root, v, tmp):
            nonlocal res
            if not root: return
            tmp = tmp + 1 if root.val == v + 1 else 1
            res = max(res, tmp)
            dfs(root.left, root.val, tmp)
            dfs(root.right, root.val, tmp)

        if not root: return 0
        res = 0
        dfs(root, root.val, 0)
        return res
