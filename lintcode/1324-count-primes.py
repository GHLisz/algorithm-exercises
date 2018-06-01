class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        if n < 2: return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n**0.5)+1):
            if s[i]:
                s[i*i:n:i] = [0] * len(s[i*i:n:i])
        return sum(s)
