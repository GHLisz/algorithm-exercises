class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        # write your code here
        n = len(A)
        pos_idx, neg_idx = 1, 0

        if sum(1 for a in A if a > 0) * 2 > n:
            pos_idx, neg_idx = 0, 1

        while pos_idx < n and neg_idx < n:
            while pos_idx < n and A[pos_idx] > 0:
                pos_idx += 2
            while neg_idx < n and A[neg_idx] < 0:
                neg_idx += 2
            if pos_idx < n and neg_idx < n:
                A[pos_idx], A[neg_idx] = A[neg_idx], A[pos_idx]
                pos_idx += 2
                neg_idx += 2
        return
