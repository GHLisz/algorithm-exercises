"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root
    @return: all the values with the highest frequency in any order
    """

    def findFrequentTreeSum(self, root):
        # Write your code here
        from collections import defaultdict

        if not root: return []
        freq = defaultdict(int)

        def get_sum(node):
            if not node: return 0
            s = node.val + get_sum(node.left) + get_sum(node.right)
            freq[s] += 1
            return s

        get_sum(root)
        mx_freq = max(freq.values())
        return [s for s in freq.keys() if freq[s] == mx_freq]
