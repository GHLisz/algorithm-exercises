class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        if not nums:
            return None

        for i in range(len(nums)):
            l = []
            l.append(i)
            sum = nums[i]
            if sum == 0:
                l.append(i)
                return l
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if sum == 0:
                    l.append(j)
                    return l
        return None
