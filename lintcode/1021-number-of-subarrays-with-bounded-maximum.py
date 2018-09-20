class Solution:
    """
    @param A: an array
    @param L: an integer
    @param R: an integer
    @return: the number of subarrays such that the value of the maximum array element in that subarray is at least L and at most R
    """

    def numSubarrayBoundedMax(self, A, L, R):
        # Write your code here
        res, dp, prev = 0, 0, -1

        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp, prev = 0, i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp

        return res
