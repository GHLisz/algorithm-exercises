class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        def accum(lis):
            total = 0
            for n in lis:
                total += n
                yield total

        self.accumlist = list(accum(nums))

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.accumlist[j]
        return self.accumlist[j] - self.accumlist[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
