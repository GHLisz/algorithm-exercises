class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        # write your code here
        if not A: return 1

        n = len(A)

        i = 0
        while i < n:
            if A[i] != (i + 1) and 1 <= A[i] <= n and A[A[i] - 1] != A[i]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
                # A[i], A[A[i] - 1] = A[A[i] - 1], A[i]  # Don't use this line
            else:
                i += 1

        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1
