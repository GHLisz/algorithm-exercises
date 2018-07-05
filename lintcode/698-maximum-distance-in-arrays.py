class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """
    def maxDiff(self, arrs):
        # write your code here
        res, start, end = 0, arrs[0][0], arrs[0][-1]
        for arr in arrs[1:]:
            res = max(res,
                      max(abs(arr[-1]-start),
                          abs(end-arr[0])))
            start = min(start, arr[0])
            end = max(end, arr[-1])
        return res
