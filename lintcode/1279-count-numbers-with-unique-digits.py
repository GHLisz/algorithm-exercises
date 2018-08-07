class Solution:
    """
    @param n: a non-negative integer
    @return: number of numbers with unique digits
    """

    def countNumbersWithUniqueDigits(self, n):
        # Write your code here
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, prd = 1, 1
        for i in range(min(n, 10)):
            prd *= choices[i]
            ans += prd
        return ans
