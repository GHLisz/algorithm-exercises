"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given tree
    @return: the binary tree in an m*n 2D string array
    """

    def printTree(self, root):
        # Write your code here
        def get_height(node):
            if not node: return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        rows = get_height(root)
        cols = 2 ** rows - 1
        res = [['' for _ in range(cols)] for _ in range(rows)]

        def traverse(node, level, pos):
            if not node: return

            left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
            index = left_padding + pos * (spacing + 1)

            res[level][index] = str(node.val)

            traverse(node.left, level + 1, pos << 1)
            traverse(node.right, level + 1, (pos << 1) + 1)

        traverse(root, 0, 0)
        return res
