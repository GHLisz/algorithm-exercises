"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        def t(root, res, paths):
            paths.append(str(root.val))
            if not any([root.left, root.right]):
                res.append('->'.join(paths))
            else:
                if root.left:
                    t(root.left, res, paths)
                if root.right:
                    t(root.right, res, paths)
            paths.pop()

        if not root: return []
        res = []
        t(root, res, [])
        return res
