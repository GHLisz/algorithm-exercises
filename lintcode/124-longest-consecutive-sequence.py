class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        nums = set(num)
        res = 0
        for begin in nums:
            if begin-1 not in nums:
                end = begin + 1
                while end in nums:
                    end += 1
                res = max(res, end-begin)
        return res
