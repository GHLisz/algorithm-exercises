class Solution:
    """
    @param A: an array
    @return: the number of arithmetic slices in the array A.
    """

    def numberOfArithmeticSlices(self, A):
        # Write your code here
        dp, total = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                total += dp
            else:
                dp = 0
        return total
