class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not dict: return not bool(s)

        ml, n = max(len(w) for w in dict), len(s)
        # dp[i] = True if (s[:i] in dict) or (dp[k] and s[k+1:i] in dict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - ml - 1, -1), -1):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[n]
