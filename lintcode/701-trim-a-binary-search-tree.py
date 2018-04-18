"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """

    def trimBST(self, root, minimum, maximum):
        # write your code here
        def trim(node):
            if not node: return None
            if node.val > maximum: return trim(node.left)
            if node.val < minimum: return trim(node.right)

            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

        return trim(root)
