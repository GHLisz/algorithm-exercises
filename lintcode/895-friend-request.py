class Solution:
    """
    @param ages: The ages
    @return: The answer
    """

    def friendRequest(self, ages):
        # Write your code here
        res, n = 0, len(ages)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = ages[i], ages[j]
                if b <= a / 2 + 7 or b > a or b < 100 < a:
                    continue
                res += 1
        return res
