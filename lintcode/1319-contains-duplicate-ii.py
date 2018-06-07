class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """

    def containsNearbyDuplicate(self, nums, k):
        # Write your code here
        def sol1():
            s = set()
            for i in range(len(nums)):
                if i > k:
                    s.remove(nums[i - k - 1])
                if nums[i] in s:
                    return True
                else:
                    s.add(nums[i])
            return False

        def sol2():
            d = {}
            for i, v in enumerate(nums):
                if v in d and d[v] >= i - k:
                    return True
                d[v] = i
            return False

        return sol2()
