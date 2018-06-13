"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """

    def str2tree(self, s):
        # write your code here
        if not s: return None

        first_paren = s.find('(')
        if first_paren == -1:
            return TreeNode(int(s))
        node = TreeNode(int(s[:first_paren]))

        start, left_paren_cnt = first_paren, 0
        for i in range(start, len(s)):
            if s[i] == '(':
                left_paren_cnt += 1
            elif s[i] == ')':
                left_paren_cnt -= 1

            if left_paren_cnt == 0 and start == first_paren:
                node.left = self.str2tree(s[start + 1:i])
                start = i + 1
            elif left_paren_cnt == 0:
                node.right = self.str2tree(s[start + 1:i])

        return node
