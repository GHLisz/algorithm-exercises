class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """

    def findUnsortedSubarray(self, nums):
        # Write your code here
        def sol1():
            n = len(nums)
            sorted_nums = sorted(nums)
            if sorted_nums == nums:
                return 0
            for i in range(n):
                if nums[i] != sorted_nums[i]:
                    break
            for j in range(n - 1, -1, -1):
                if nums[j] != sorted_nums[j]:
                    break
            return j - i + 1

        def sol2():
            n = len(nums)
            mx, mn = nums[0], nums[-1]
            end, start = -2, -1
            for i in range(1, n):
                mx = max(mx, nums[i])
                if mx > nums[i]:
                    end = i
                mn = min(mn, nums[n - 1 - i])
                if mn < nums[n - 1 - i]:
                    start = n - 1 - i
            return end - start + 1

        return sol2()
