"""
103. Binary Tree Zigzag Level Order Traversal
Medium


Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def trav(res, node, depth):
            if not node:
                return

            if len(res) == depth:
                res.append([])

            if depth % 2 == 0:
                res[depth].append(node.val)
            else:
                res[depth].insert(0, node.val)

            trav(res, node.left, depth + 1)
            trav(res, node.right, depth + 1)

        res = []
        trav(res, root, 0)
        return res
