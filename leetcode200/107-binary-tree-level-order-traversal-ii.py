"""
107. Binary Tree Level Order Traversal II
Easy


Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def trav(node, level, res):
            if not node:
                return
            if len(res) == level:
                res.append([])

            res[level].append(node.val)

            for child in filter(bool, [node.left, node.right]):
                trav(child, level + 1, res)

        res = []
        trav(root, 0, res)
        res.reverse()
        return res
