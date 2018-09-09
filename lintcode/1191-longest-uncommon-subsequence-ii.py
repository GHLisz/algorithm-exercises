class Solution:
    """
    @param strs: List[str]
    @return: return an integer
    """

    def findLUSlength(self, strs):
        # write your code here
        def is_sub(s, t):
            t = iter(t)
            return all(c in t for c in s)

        for s in sorted(strs, key=len, reverse=True):
            if sum(is_sub(s, t) for t in strs) == 1:
                return len(s)

        return -1
