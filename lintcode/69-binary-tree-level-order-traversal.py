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
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        if root is None: return []

        res, q = [], [root]

        while q:
            new_q = []
            res.append([node.val for node in q])
            for node in q:
                for sub in filter(bool, [node.left, node.right]):
                    new_q.append(sub)
            q = new_q
        return res
