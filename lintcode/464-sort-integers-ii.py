class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        p, r = 0, len(A) - 1
        self.quick_sort(A, p, r)

    def quick_sort(self, A, p, r):
        if p < r:
            q = self.partition(A, p, r)
            self.quick_sort(A, p, q - 1)
            self.quick_sort(A, q + 1, r)

    def partition(self, A, p, r):
        piv = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= piv:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1
