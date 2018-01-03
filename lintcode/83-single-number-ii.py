class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """

    def singleNumberII(self, A):
        # write your code here
        ones, twos = 0, 0
        for i in range(len(A)):
            ones = (ones ^ A[i]) & ~twos
            twos = (twos ^ A[i]) & ~ones
        return ones
