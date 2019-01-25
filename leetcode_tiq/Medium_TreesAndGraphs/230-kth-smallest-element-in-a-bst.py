"""
230. Kth Smallest Element in a BST
Medium


Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def sol1(root, k):  # binary search
            def children_count(node):
                if not node:
                    return 0
                return 1 + sum(map(children_count, [node.left, node.right]))

            count = children_count(root.left)
            if k <= count:
                return sol1(root.left, k)
            elif k > count + 1:
                return sol1(root.right, k - 1 - count)
            return root.val

        def sol2(root, k):  # recursive, for the follow up
            def helper(node, count):
                if not node:
                    return
                helper(node.left, count)
                count.append(node.val)
                helper(node.right, count)

            count = []
            helper(root, count)
            return count[k - 1]

        def sol3(root, k):  # iterative dfs in-order
            stk = []
            while root:
                stk.append(root)
                root = root.left

            while k != 0:
                node = stk.pop()
                k -= 1
                if k == 0:
                    return node.val
                right = node.right
                while right:
                    stk.append(right)
                    right = right.left
            return -1

        return sol3(root, k)
