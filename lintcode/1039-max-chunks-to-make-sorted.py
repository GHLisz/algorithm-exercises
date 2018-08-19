class Solution:
    """
    @param arr: a permutation of N
    @return: the most number of chunks
    """

    def maxChunksToSorted(self, arr):
        # write your code here
        res = mx = 0
        for i, x in enumerate(arr):
            mx = max(mx, x)
            res += 1 if mx == i else 0
        return res
