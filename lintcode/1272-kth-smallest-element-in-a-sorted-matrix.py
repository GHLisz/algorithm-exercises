class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """

    def kthSmallest(self, matrix, k):
        # write your code here
        import bisect

        n, mid = len(matrix), 0
        lo, hi = matrix[0][0], matrix[-1][-1]

        while lo < hi:
            mid = (lo + hi) // 2
            num = 0
            for i in range(n):
                pos = bisect.bisect_right(matrix[i], mid)
                num += pos
            if num < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
