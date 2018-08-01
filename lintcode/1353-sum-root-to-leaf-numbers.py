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
            ns = 10 * s + node.val
            if not any([node.left, node.right]): return ns
            return count(node.left, ns) + count(node.right, ns)

        return count(root, 0)
