"""
215. Kth Largest Element in an Array
Medium


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def sol1():  # sort
            return sorted(nums)[-k]

        def sol2():  # min heap
            import heapq
            min_heap = [-float('inf')] * k
            for num in nums:
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
            return min_heap[0]

        def sol3():  # quick select
            def partition(A, l, r):
                piv, i = A[r], l - 1
                for j in range(l, r):
                    if A[j] <= piv:
                        i += 1
                        A[i], A[j] = A[j], A[i]
                A[i + 1], A[r] = A[r], A[i + 1]
                return i + 1

            def quick_select(A, k, l, r):
                if l >= r:
                    return A[l]
                m = partition(A, l, r)
                if m == k:
                    return A[m]
                elif m < k:
                    return quick_select(A, k, m + 1, r)
                else:
                    return quick_select(A, k, l, m - 1)

            return quick_select(nums, len(nums) - k, 0, len(nums) - 1)

        return sol3()
