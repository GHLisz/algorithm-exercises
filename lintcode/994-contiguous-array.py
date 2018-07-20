class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """

    def findMaxLength(self, nums):
        # Write your code here
        dic, max_len, count = {0: -1}, 0, 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in dic:
                max_len = max(max_len, i - dic[count])
            else:
                dic[count] = i
        return max_len
