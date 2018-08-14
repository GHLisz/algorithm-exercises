"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        def traverse(node, res):
            if not node: return
            res.append(node.val)
            traverse(node.left, res)
            traverse(node.right, res)

        res = []
        traverse(root, res)
        return res
