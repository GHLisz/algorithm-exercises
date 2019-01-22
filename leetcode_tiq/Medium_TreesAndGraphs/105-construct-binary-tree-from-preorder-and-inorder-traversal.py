"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def sol1(preorder, inorder):  # recursive
            if not preorder:
                return None

            root = TreeNode(preorder[0])
            rt_idx = inorder.index(preorder[0])
            root.left = sol1(preorder[1:rt_idx + 1], inorder[:rt_idx])
            root.right = sol1(preorder[rt_idx + 1:], inorder[rt_idx + 1:])
            return root

        def sol2(preorder, inorder):  # iterative
            if not preorder:
                return None

            root = TreeNode(preorder[0])
            stk, preo, ino = [root], 1, 0

            while preo < len(preorder):
                curr = TreeNode(preorder[preo])
                preo += 1
                prev = None
                while stk and stk[-1].val == inorder[ino]:
                    prev = stk.pop()
                    ino += 1
                if prev:
                    prev.right = curr
                else:
                    stk[-1].left = curr

                stk.append(curr)
            return root

        return sol2(preorder, inorder)
