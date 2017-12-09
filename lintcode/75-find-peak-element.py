class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here
        def binary(nums, start, end):
            if start == end:
                return start
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                return binary(nums, start, mid - 1)
            else:
                return binary(nums, mid + 1, end)

        return binary(A, 0, len(A) - 1)
