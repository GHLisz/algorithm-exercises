"""
20. Valid Parentheses
Easy


Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk, pair = [], {')': '(', '}': '{', ']': '[', }
        for c in s:
            if c in pair.values():
                stk.append(c)
            elif c in pair.keys():
                if not stk or stk.pop() != pair[c]:
                    return False
            else:
                return False
        return not stk
