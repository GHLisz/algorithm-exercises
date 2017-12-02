class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        return self.helper(A, len(A) - k, 0, len(A) - 1)

    def helper(self, A, k, p, r):
        if p >= r:
            return A[p]
        m = self.partition(A, p, r)
        if m == k:
            return A[m]
        elif m < k:
            return self.helper(A, k, m + 1, r)
        else:
            return self.helper(A, k, p, m - 1)

    def partition(self, A, p, r):
        piv = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= piv:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1
