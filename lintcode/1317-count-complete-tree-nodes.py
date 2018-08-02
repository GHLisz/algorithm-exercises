"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of complete binary tree
    @return: the number of nodes
    """

    def countNodes(self, root):
        # write your code here
        # O(log(n)^2)
        def get_height(node):
            return -1 if not node else 1 + get_height(node.left)

        nodes, h = 0, get_height(root)
        while root:
            if get_height(root.right) == h - 1:
                nodes += 1 << h
                root = root.right
            else:
                nodes += 1 << h - 1
                root = root.left
            h -= 1
        return nodes
