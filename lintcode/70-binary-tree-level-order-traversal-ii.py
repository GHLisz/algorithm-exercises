"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        # write your code here
        def traverse(root, level, res):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                traverse(root.left, level + 1, res)
            if root.right:
                traverse(root.right, level + 1, res)

        res = []
        traverse(root, 0, res)
        res.reverse()
        return res
