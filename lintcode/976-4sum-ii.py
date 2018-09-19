class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """

    def fourSumCount(self, A, B, C, D):
        # Write your code here
        from collections import Counter

        AB = Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)
