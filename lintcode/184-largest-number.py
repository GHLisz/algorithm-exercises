class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """

    def largestNumber(self, nums):
        # write your code here
        from functools import cmp_to_key
        comp = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(comp), reverse=True)
        return str(int("".join(nums)))
