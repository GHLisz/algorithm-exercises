"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """

    def findSecondMinimumValue(self, root):
        # Write your code here
        def t(node):
            if node:
                uniques.add(node.val)
                t(node.left)
                t(node.right)

        uniques = set()
        t(root)

        m1, m2 = root.val, float('inf')
        for v in uniques:
            if m1 < v < m2:
                m2 = v

        return -1 if m2 == float('inf') else m2
