class Solution:
    """
    @param A: An integer array
    @param B: An integer array
    @return: Their smallest difference.
    """

    def smallestDifference(self, A, B):
        # write your code here
        A, B = map(sorted, (A, B))

        ai, bi, diff = 0, 0, float('inf')
        while ai < len(A) and bi < len(B):
            diff = min(diff, abs(A[ai] - B[bi]))
            if A[ai] < B[bi]:
                ai += 1
            elif A[ai] > B[bi]:
                bi += 1
            else:
                break
        return diff
