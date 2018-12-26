"""
102. Binary Tree Level Order Traversal
Medium


Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def sol1():  # dfs, recursive
            def trav(node, depth, res):
                if not node:
                    return
                if len(res) == depth:
                    res.append([])

                res[depth].append(node.val)

                for child in filter(bool, [node.left, node.right]):
                    trav(child, depth + 1, res)

            res = []
            trav(root, 0, res)
            return res

        def sol2():  # bfs, iterative
            if not root:
                return []

            res, q = [], [root]

            while q:
                new_q = []
                res.append([node.val for node in q])
                for node in q:
                    for child in filter(bool, [node.left, node.right]):
                        new_q.append(child)
                q = new_q

            return res

        return sol2()
