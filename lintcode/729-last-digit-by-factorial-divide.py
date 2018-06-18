class Solution:
    """
    @param A: the given number
    @param B: another number
    @return: the last digit of B! / A!
    """

    def computeLastDigit(self, A, B):
        # write your code here
        if A == B: return 1
        if (B - A) >= 5: return 0

        var = 1
        for i in range(A + 1, B + 1):
            var = (var * (i % 10)) % 10

        return var % 10
