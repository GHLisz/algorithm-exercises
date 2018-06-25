class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        def partition(A, p, r):
            piv = A[r]
            i = p - 1
            for j in range(p, r):
                if A[j] <= piv:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            A[i + 1], A[r] = A[r], A[i + 1]
            return i + 1

        def quick_sort(A, p, r):
            if p < r:
                q = partition(A, p, r)
                quick_sort(A, p, q - 1)
                quick_sort(A, q + 1, r)

        p, r = 0, len(A) - 1
        quick_sort(A, p, r)
