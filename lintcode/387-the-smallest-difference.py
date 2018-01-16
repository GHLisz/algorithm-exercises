class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Their smallest difference.
    """
    def smallestDifference(self, A, B):
        # write your code here
        A.sort()
        B.sort()

        ai, bi, res = 0, 0, 999999**2
        while ai < len(A) and bi < len(B):
            res = min(res, abs(A[ai]-B[bi]))
            if A[ai] < B[bi]:
                ai += 1
            elif A[ai] > B[bi]:
                bi += 1
            else:
                break
        return res
