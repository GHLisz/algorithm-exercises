class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        dp = [0] * (m+1)  # dp[m]: how full of size m backpack
        for i in range(len(A)):
            for j in range(m, -1, -1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j-A[i]]+A[i])
        return dp[m]
