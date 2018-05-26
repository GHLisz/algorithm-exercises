class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        import math
        m1 = m2 = -math.inf
        for num in nums:
            if num >= m1:
                m1, m2 = num, m1
            elif m2 <= num < m1:
                m2 = num
            else:
                continue
        return m2
