class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        # Write your code here
        # lo, hi: smallest and largest possible number of open left brackets
        # after processing the current character
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)
        return lo == 0
