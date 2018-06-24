class Solution:
    """
    @param n: a integer, denote the number of teams
    @return: a string
    """
    def findContestMatch(self, n):
        # write your code here
        m = list(range(1, n + 1))
        while n > 1:
            for i in range(n // 2):
                m[i] = f'({m[i]},{m[n-i-1]})'
            n //= 2
        return m[0]
