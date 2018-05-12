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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        # write your code here
        def preorder(root, level, res):
            if root:
                if len(res) < level + 1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(root.val)
                else:
                    res[level].insert(0, root.val)
                preorder(root.left, level + 1, res)
                preorder(root.right, level + 1, res)

        res = []
        preorder(root, 0, res)
        return res
