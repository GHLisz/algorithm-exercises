class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """

    def findTheDifference(self, s, t):
        # Write your code here
        def sol1():
            from collections import Counter
            sc, tc = Counter(s), Counter(t)
            for k, v in tc.items():
                if sc[k] != v:
                    return k
            return None

        def sol2():
            res = 0
            for c in s: res ^= ord(c)
            for c in t: res ^= ord(c)
            return chr(res)

        return sol1()
