class Solution:
    """
    @param: A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
        from operator import xor
        diff = reduce(xor, A, 0)
        diff &= -diff
        res = [0, 0]
        for num in A:
            if num & diff:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
