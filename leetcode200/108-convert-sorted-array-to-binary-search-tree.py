"""
108. Convert Sorted Array to Binary Search Tree
Easy


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def convert(arr, start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(arr[start])

            mid = (start + end) // 2
            root = TreeNode(arr[mid])
            root.left = convert(arr, start, mid - 1)
            root.right = convert(arr, mid + 1, end)
            return root

        return convert(nums, 0, len(nums) - 1)
