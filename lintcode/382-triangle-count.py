class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        ans, n = 0, len(S)
        S.sort()

        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if S[i] + S[j] > S[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans
