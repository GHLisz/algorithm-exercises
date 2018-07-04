class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here
        dp, words_set, word_max_len = [True], set(dict), max(map(len, dict), default=0)
        for i in range(1, len(s) + 1):
            dp += any(dp[j] and s[j:i] in words_set
                      for j in range(max(0, i - word_max_len), i)),
        return dp[-1]
