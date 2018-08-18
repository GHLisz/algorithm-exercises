"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """

    def checkEqualTree(self, root):
        # write your code here
        sub_sums = []

        def get_sum(node):
            if not node: return 0
            sub_sums.append(get_sum(node.left) + get_sum(node.right) + node.val)
            return sub_sums[-1]

        total = get_sum(root)
        sub_sums.pop()
        return total / 2 in sub_sums
