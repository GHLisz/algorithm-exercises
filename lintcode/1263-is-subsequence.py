class Solution:
    """
    @param s: the given string s
    @param t: the given string t
    @return: check if s is subsequence of t
    """

    def isSubsequence(self, s, t):
        # Write your code here
        it = iter(t)
        return all(c in it for c in s)
