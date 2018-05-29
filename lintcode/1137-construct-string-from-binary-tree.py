"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        if not t: return ''
        left = f'({self.tree2str(t.left)})' if (t.left or t.right) else ''
        right = f'({self.tree2str(t.right)})' if t.right else ''
        return f'{t.val}{left}{right}'
