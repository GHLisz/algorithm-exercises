"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a root of integer
    @return: return a integer
    """

    def findMode(self, root):
        # write your code here
        from collections import Counter
        cnt = Counter()

        def t(node):
            if node:
                cnt[node.val] += 1
                t(node.left)
                t(node.right)

        t(root)
        mfq = max(cnt.values())
        return sorted([k for k, v in cnt.items() if v == mfq])
