class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        # write your code here
        def sol1():  # two pointers, n
            slow, fast = nums[0], nums[nums[0]]
            while slow != fast:
                slow, fast = nums[slow], nums[nums[fast]]
            fast = 0
            while fast != slow:
                fast, slow = nums[fast], nums[slow]
            return slow

        def sol2():  # binary, nlogn TLE
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                cnt = sum(1 for num in nums if num <= m)
                if cnt > m:
                    r = m - 1
                else:
                    l = m + 1
            return l

        return sol1()
