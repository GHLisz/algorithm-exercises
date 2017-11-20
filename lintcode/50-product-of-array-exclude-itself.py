class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        if not nums:
            return []
        len_nums = len(nums)
        left = [1] * len_nums
        right = [1] * len_nums
        B = [0 for _ in range(len_nums)]
        for i in range(1, len_nums):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len_nums-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(len_nums):
            B[i] = left[i] * right[i]
        return B
