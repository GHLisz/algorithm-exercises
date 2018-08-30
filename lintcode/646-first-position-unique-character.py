class Solution:
    """
    @param s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        from collections import Counter

        counter = Counter(ord(c) for c in s)
        return next((k for k, v in enumerate(s) if counter[ord(v)] == 1), -1)
