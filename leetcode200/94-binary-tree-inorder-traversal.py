"""
94. Binary Tree Inorder Traversal
Medium


Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def sol1():  # recursive
            def trav(node, res):
                if not node:
                    return
                trav(node.left, res)
                res.append(node.val)
                trav(node.right, res)

            res = []
            trav(root, res)
            return res

        def sol2():  # iterative
            nonlocal root
            res, stack = [], []
            while True:
                while root:
                    stack.append(root)
                    root = root.left
                if not stack:
                    return res
                node = stack.pop()
                res.append(node.val)
                root = node.right

        return sol2()
