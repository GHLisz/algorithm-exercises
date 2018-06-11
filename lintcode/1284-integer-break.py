class Solution:
    """
    @param n: a positive integer n
    @return: the maximum product you can get
    """

    def integerBreak(self, n):
        # Write your code here
        def sol1(n):
            dp = [1] + [0] * n
            for i in range(2, n + 1):
                for j in range(1, i):
                    dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
            return dp[n]

        def sol2(n):
            # https://leetcode.com/problems/integer-break/discuss/80689/A-simple-explanation-of-the-math-part-and-a-O(n)-solution
            if n == 2: return 1
            if n == 3: return 2
            product = 1
            while n > 4:
                product *= 3
                n -= 3
            product *= n
            return product

        return sol1(n)
