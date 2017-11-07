"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        result = []
        if not root:
            return result

        path_stack = []
        self.valid_path(result, root, 0, target, path_stack)
        return result

    def valid_path(self, result, root, cur_sum, target, path_stack):
        cur_sum += root.val
        path_stack.append(root.val)

        if cur_sum == target and root.left is None and root.right is None:
            result.append([node for node in path_stack])
            path_stack.pop()
        else:
            if root.left:
                self.valid_path(result, root.left, cur_sum, target, path_stack)
            if root.right:
                self.valid_path(result, root.right, cur_sum, target, path_stack)
            path_stack.pop()

