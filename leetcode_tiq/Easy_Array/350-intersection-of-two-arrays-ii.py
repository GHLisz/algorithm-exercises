"""
350. Intersection of Two Arrays II
Easy


Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        def sol1():  # already sorted
            nums1.sort()
            nums2.sort()

            res, i, j = [], 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    i, j = i + 1, j + 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            return res

        def sol2():  # nums1's size smaller or nums2 on disk
            from collections import Counter

            res, c = [], Counter(nums1)
            for n in nums2:
                if c[n] > 0:
                    res.append(n)
                    c[n] -= 1
            return res

        return sol2()
