class Solution:
    """
    @param: nums: a list of n integers
    @return: true if there is a 132 pattern or false
    """
    def find132pattern(self, nums):
        # write your code here
        third = -99999
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < third:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    third = stack[-1]
                    stack.pop()
            stack.append(nums[i])
        return False
