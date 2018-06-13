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
    @return: a list of integer
    """

    def boundaryOfBinaryTree(self, root):
        # write your code here
        def t(node, is_left_bd, is_right_bd):
            nonlocal res
            if not node: return
            if not any([node.left, node.right]):
                res.append(node.val)
                return

            if is_left_bd: res.append(node.val)
            t(node.left, is_left_bd and node.left, is_right_bd and (not node.right))
            t(node.right, is_left_bd and (not node.left), is_right_bd and node.right)
            if is_right_bd: res.append(node.val)

        if not root: return []
        res = [root.val]
        t(root.left, True, False)
        t(root.right, False, True)
        return res
