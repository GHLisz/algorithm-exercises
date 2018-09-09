class Solution:
    """
    @param k: An integer
    @param A: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, A):
        # write your code here
        def sol1():  # quick_select
            def partition(A, p, r):
                piv, i = A[r], p - 1
                for j in range(p, r):
                    if A[j] <= piv:
                        i += 1
                        A[i], A[j] = A[j], A[i]
                A[i + 1], A[r] = A[r], A[i + 1]
                return i + 1

            def quick_select(A, k, p, r):
                if p >= r: return A[p]
                m = partition(A, p, r)
                if m == k:
                    return A[m]
                elif m < k:
                    return quick_select(A, k, m + 1, r)
                else:
                    return quick_select(A, k, p, m - 1)

            return quick_select(A, len(A) - k, 0, len(A) - 1)

        def sol2():  # heap
            import heapq
            heap = A[:]
            heapq.heapify(heap)
            for _ in range(len(heap) - k):
                heapq.heappop(heap)
            return heapq.heappop(heap)

        return sol2()
