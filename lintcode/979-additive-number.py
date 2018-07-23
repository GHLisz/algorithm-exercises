class Solution:
    """
    @param num: a string
    @return: Is it a valid additive number
    """

    def isAdditiveNumber(self, num):
        # Write your code here
        from itertools import combinations
        n = len(num)
        for i, j in combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            if b != str(int(b)):
                continue
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                j += len(c)
                a, b = b, c
            if j == n:
                return True
        return False
