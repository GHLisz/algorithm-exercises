"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """

    def sumNumbers(self, root):
        # write your code here
        def count(node, s):
            if not node: return 0
            new_s = 10 * s + node.val
            if not any([node.left, node.right]):
                return new_s
            return count(node.left, new_s) + count(node.right, new_s)

        return count(root, 0)
