class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here
        def partition(nums, start, end, size):
            mid = (start + end) / 2
            pivot = nums[mid]
            i, j = start - 1, end + 1

            k = start
            while k < j:
                if nums[k] < pivot:
                    i += 1
                    nums[i], nums[k] = nums[k], nums[i]
                elif nums[k] > pivot:
                    j -= 1
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
                k += 1

            if (i - start + 1) >= size:
                return partition(nums, start, i, size)
            elif (j - start) >= size:
                return nums[j - 1]
            else:
                return partition(nums, j, end, size - (j - start))

        return partition(nums, 0, len(nums) - 1, (len(nums) + 1) / 2)
