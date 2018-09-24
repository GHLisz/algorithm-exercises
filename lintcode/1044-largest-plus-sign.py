class Solution:
    """
    @param N: size of 2D grid
    @param mines: in the given list
    @return: the order of the plus sign
    """

    def orderOfLargestPlusSign(self, N, mines):
        # Write your code here
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0

        for r in range(N):
            count = 0
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            count = 0
            for c in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(count, dp[r][c])

        for c in range(N):
            count = 0
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(count, dp[r][c])

            count = 0
            for r in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(count, dp[r][c])
                ans = max(ans, dp[r][c])

        return ans
