class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, nums):
        # write your code here
        from operator import mul
        from itertools import accumulate

        if not nums: return []
        left = list(accumulate(nums, mul))
        right = list(accumulate(nums[::-1], mul))[::-1]
        return [l * r for l, r in zip([1] + left[:-1], right[1:] + [1])]
