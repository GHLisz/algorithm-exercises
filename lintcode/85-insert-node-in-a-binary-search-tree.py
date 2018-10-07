"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        def recursive(root, node):
            if not node: return root
            if not root: return node

            if node.val < root.val:
                root.left = recursive(root.left, node)
            else:
                root.right = recursive(root.right, node)
            return root

        def iterative(root, node):
            if not root: return node

            cur = root
            while cur != node:
                if node.val < cur.val:
                    if cur.left is None:
                        cur.left = node
                    cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = node
                    cur = cur.right
            return root

        return iterative(root, node)
