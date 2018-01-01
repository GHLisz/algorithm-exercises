class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        dp = [0 for _ in range(m+1)]
        for i in range(len(A)):
            for j in range(m, A[i]-1, -1):
                dp[j] = max(dp[j], dp[j-A[i]] + V[i])
        return dp[m]
