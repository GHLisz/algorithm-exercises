class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # write your code here
        def parent(i):
            return (i - 1) // 2

        def left(i):
            return 2 * i + 1

        def right(i):
            return 2 * i + 2

        def min_heapify(A, i):
            heap_size = len(A)
            l, r = left(i), right(i)
            smallest = i
            if l < heap_size and A[l] < A[smallest]:
                smallest = l
            if r < heap_size and A[r] < A[smallest]:
                smallest = r
            if smallest != i:
                A[i], A[smallest] = A[smallest], A[i]
                min_heapify(A, smallest)

        heap_size = len(A)
        for i in range(parent(heap_size - 1), -1, -1):
            min_heapify(A, i)
        return A
