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
        def recursive():
            def trav(node, res):
                if not node: return

                res.append(node.val)
                trav(node.left, res)
                trav(node.right, res)

            res = []
            trav(root, res)
            return res

        def iterative():
            if not root: return []

            res, stack = [], [root]

            while stack:
                node = stack.pop()
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return res

        return iterative()
