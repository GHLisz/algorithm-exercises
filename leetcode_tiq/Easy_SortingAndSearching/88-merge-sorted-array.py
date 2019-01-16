"""
88. Merge Sorted Array
Easy


Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        arr1, arr2 = nums1[:m] + [float('inf')], nums2[:n] + [float('inf')]

        i1, i2 = 0, 0
        for k in range(m + n):
            if arr1[i1] < arr2[i2]:
                nums1[k] = arr1[i1]
                i1 += 1
            else:
                nums1[k] = arr2[i2]
                i2 += 1
