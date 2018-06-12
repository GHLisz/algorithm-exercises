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
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder: return None
        root = TreeNode(preorder[0])
        rt_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rt_idx+1], inorder[:rt_idx])
        root.right = self.buildTree(preorder[rt_idx+1:], inorder[rt_idx+1:])
        return root
