class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        # write your code here
        tmp = [0] * len(A)

        def merge_sort(A, l, r):
            if l >= r: return 0

            m = (l + r) // 2
            ans = merge_sort(A, l, m) + merge_sort(A, m + 1, r)

            i, j, k = l, m + 1, l
            while i <= m and j <= r:
                if A[i] > A[j]:
                    tmp[k] = A[j]
                    j += 1
                    ans += m - i + 1
                else:
                    tmp[k] = A[i]
                    i += 1
                k += 1

            while i <= m:
                tmp[k] = A[i]
                k += 1
                i += 1
            while j <= r:
                tmp[k] = A[j]
                k += 1
                j += 1
            for i in range(l, r + 1):
                A[i] = tmp[i]

            return ans

        return merge_sort(A, 0, len(A) - 1)
