"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        result = []
        if root is None:
            return result
        path_stack = []
        self.helper(root, result, path_stack)
        return result

    def helper(self, root, result, path_stack):
        path_stack.append(str(root.val))

        if root.left is None and root.right is None:
            result.append('->'.join(path_stack))
            path_stack.pop()
        else:
            if root.left:
                self.helper(root.left, result, path_stack)
            if root.right:
                self.helper(root.right, result, path_stack)
            path_stack.pop()
