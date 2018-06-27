"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber3(self, root):
        # write your code here
        def rob(root):
            res = [0, 0]    # [not robbed, robbed]
            if not root: return res
            left, right = rob(root.left), rob(root.right)
            res[0] = max(left) + max(right)
            res[1] = root.val + left[0] + right[0]
            return res

        return max(rob(root))
