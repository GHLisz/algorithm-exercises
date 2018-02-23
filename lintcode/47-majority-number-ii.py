class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """

    def majorityNumber(self, nums):
        # write your code here
        cd1, c1, cd2, c2 = None, 0, None, 0
        for num in nums:
            if cd1 == num:
                c1 += 1
            elif cd2 == num:
                c2 += 1
            elif c1 == 0:
                c1 += 1
                cd1 = num
            elif c2 == 0:
                c2 += 1
                cd2 = num
            else:
                c1 -= 1
                c2 -= 1

        c1, c2 = 0, 0
        for num in nums:
            if cd1 == num:
                c1 += 1
            elif cd2 == num:
                c2 += 1

        return cd1 if c1 > c2 else cd2
