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

        def convert(arr, low, high):
            if low > high:
                return None
            if low == high:
                return TreeNode(arr[low])

            mid = (low + high) // 2
            node = TreeNode(arr[mid])
            node.left = convert(arr, low, mid - 1)
            node.right = convert(arr, mid + 1, high)
            return node

        return convert(nums, 0, len(nums) - 1)
