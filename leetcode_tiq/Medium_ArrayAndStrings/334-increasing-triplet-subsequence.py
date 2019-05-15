"""
334. Increasing Triplet Subsequence
Medium


Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        def sol1():
            first = second = float('inf')
            for n in nums:
                if n <= first:
                    first = n
                elif n <= second:
                    second = n
                else:
                    return True
            return False

        def sol2():  # generalized
            import bisect

            k = 3
            inc = [float('inf')] * (k - 1)
            for n in nums:
                i = bisect.bisect_left(inc, n)
                if i >= k - 1:
                    return True
                inc[i] = n
            return k == 0

        return sol2()
