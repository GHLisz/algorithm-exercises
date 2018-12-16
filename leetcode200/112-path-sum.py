"""
112. Path Sum
Easy


Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, total):
        """
        :type root: TreeNode
        :type total: int
        :rtype: bool
        """
        if not root:
            return False

        if all([not root.left, not root.right, root.val == total]):
            return True

        total -= root.val

        return self.hasPathSum(root.left, total) or self.hasPathSum(root.right, total)
