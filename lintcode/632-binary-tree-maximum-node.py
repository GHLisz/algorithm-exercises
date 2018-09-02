"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        # write your code here
        if not root: return root

        max_node = root
        for sub in filter(bool, [root.left, root.right]):
            sub_res = self.maxNode(sub)
            max_node = max_node if max_node.val > sub_res.val else sub_res

        return max_node
