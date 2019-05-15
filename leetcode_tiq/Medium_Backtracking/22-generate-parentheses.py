"""
22. Generate Parentheses
Medium


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(l, r, item, res):
            if l > r:
                return
            if l == 0 and r == 0:
                res.append(item)
            if l > 0:
                gen(l - 1, r, item + '(', res)
            if r > 0:
                gen(l, r - 1, item + ')', res)

        res = []
        gen(n, n, '', res)
        return res
