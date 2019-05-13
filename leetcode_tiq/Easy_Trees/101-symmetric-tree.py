"""
101. Symmetric Tree
Easy


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def sol1():  # recursive
            def is_mirror(left, right):
                if not left:
                    return not right
                if not right:
                    return not left
                return left.val == right.val \
                       and is_mirror(left.left, right.right) \
                       and is_mirror(left.right, right.left)
            return is_mirror(root, root)

        def sol2():  # iterative
            if not root:
                return True

            stk = [(root.left, root.right)]

            while stk:
                p0, p1 = stk.pop()
                if (not p0) and (not p1):
                    continue
                if (not p0) or (not p1) or p0.val != p1.val:
                    return False
                stk.append((p0.right, p1.left))
                stk.append((p0.left, p1.right))
            return True

        return sol2()
