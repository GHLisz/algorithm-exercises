class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        # write your code here
        def get_lcp(s1, s2):
            end, length = 0, min(len(s1), len(s2))
            while end < length:
                if s1[end] != s2[end]: break
                end += 1
            return s1[:end]

        if not strs: return ''
        lcp = strs[0]
        for s in strs[1:]:
            lcp = get_lcp(s, lcp)
            if not lcp: return ''
        return lcp
