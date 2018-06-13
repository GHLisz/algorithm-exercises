"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        def solve(root):
            nonlocal ans
            inc = dec = 0
            for child in (root.left, root.right):
                if not child: continue
                cinc, cdec = solve(child)
                if child.val == root.val - 1:
                    dec = max(dec, cdec)
                elif child.val == root.val + 1:
                    inc = max(inc, cinc)
            ans = max(ans, inc + dec + 1)
            return inc + 1, dec + 1

        ans = 0
        if root: solve(root)
        return ans
