"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if not root:
            return
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)
