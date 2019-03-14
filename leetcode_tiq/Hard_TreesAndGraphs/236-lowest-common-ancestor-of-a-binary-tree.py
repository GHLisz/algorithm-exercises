"""
236. Lowest Common Ancestor of a Binary Tree
Medium


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def sol1(root, p, q):  # iterative using parent pointers
            stack, parent = [root], {root: None}
            while p not in parent or q not in parent:
                node = stack.pop()
                for kid in filter(bool, [node.left, node.right]):
                    parent[kid] = node
                    stack.append(kid)
            ancestors = set()
            while p:
                ancestors.add(p)
                p = parent[p]
            while q not in ancestors:
                q = parent[q]
            return q

        def sol2(root, p, q):  # recursive
            if root in (None, p, q):
                return root
            left, right = [sol2(kid, p, q) for kid in (root.left, root.right)]
            return root if (left and right) else (left or right)

        return sol1(root, p, q)
