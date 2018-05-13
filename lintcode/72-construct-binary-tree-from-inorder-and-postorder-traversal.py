"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        def build(ileft, iright, pleft, pright):
            if ileft > iright or pleft > pright: return None
            cur, i = TreeNode(postorder[pright]), 0
            for i in range(ileft, len(inorder)):
                if inorder[i] == cur.val: break
            cur.left = build(ileft, i-1, pleft, pleft+i-ileft-1)
            cur.right = build(i+1, iright, pleft+i-ileft, pright-1)
            return cur
        return build(0, len(inorder)-1, 0, len(postorder)-1)
