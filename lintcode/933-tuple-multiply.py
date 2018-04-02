class Solution:
    """
    @param tuple: the tuple string
    @param n: an integer
    @return: the product of all the nth element in each array
    """
    def tupleMultiply(self, tuple, n):
        # Write your code here
        import re
        nums = re.findall(r'\((.*?)\)', tuple)
        ans = 1
        for i in nums:
            ans = ans * int(i.split(',')[n - 1])
        return ans
