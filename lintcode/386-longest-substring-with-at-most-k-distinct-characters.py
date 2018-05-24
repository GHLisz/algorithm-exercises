class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        res, left, m = 0, 0, collections.defaultdict(int)
        for i in range(len(s)):
            m[s[i]] += 1
            while len(m) > k:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res
