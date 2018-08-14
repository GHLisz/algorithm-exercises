class Solution:
    """
    @param word1: a string
    @param word2: a string
    @return: return a integer
    """

    def minDistance(self, word1, word2):
        # write your code here
        def sol1():
            dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
            for i in range(len(word1) + 1):
                for j in range(len(word2) + 1):
                    if i == 0 or j == 0:
                        dp[i][j] = i + j
                    elif word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
            return dp[len(word1)][len(word2)]

        def sol2():
            dp = [0] * (len(word2) + 1)
            for i in range(len(word1) + 1):
                tmp = [0] * (len(word2) + 1)
                for j in range(len(word2) + 1):
                    if i == 0 or j == 0:
                        tmp[j] = i + j
                    elif word1[i - 1] == word2[j - 1]:
                        tmp[j] = dp[j - 1]
                    else:
                        tmp[j] = 1 + min(dp[j], tmp[j - 1])
                dp = tmp
            return dp[len(word2)]

        return sol2()
