"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """

    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        def sol1():  # O(n^2) recursive
            def construct(nums):
                if not nums: return None
                root, maxi = TreeNode(max(nums)), nums.index(max(nums))
                root.left = self.constructMaximumBinaryTree(nums[:maxi])
                root.right = self.constructMaximumBinaryTree(nums[maxi + 1:])
                return root

            return construct(nums)

        def sol2():  # O(n) stack
            stack = []
            for i in range(len(nums)):
                cur = TreeNode(nums[i])
                while stack and stack[-1].val < nums[i]:
                    cur.left = stack.pop()
                if stack:
                    stack[-1].right = cur
                stack.append(cur)
            return stack[0] if stack else None

        def sol3():  # O(n) stack, avoid emptiness checks
            stack = [TreeNode(float('inf'))]
            for num in nums:
                cur = TreeNode(num)
                while stack[-1].val < num:
                    cur.left = stack.pop()
                stack[-1].right = cur
                stack.append(cur)
            return stack[1]

        return sol3()
