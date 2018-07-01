class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """
    def maxDiff(self, arrs):
        # write your code here
        res, start, end = 0, arrs[0][0], arrs[0][-1]
        for i in range(1, len(arrs)):
            res = max(res, max(abs(arrs[i][-1]-start),
                               abs(end-arrs[i][0])))
            start = min(start, arrs[i][0])
            end = max(end, arrs[i][-1])
        return res
