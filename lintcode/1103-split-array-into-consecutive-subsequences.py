class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """

    def isPossible(self, nums):
        # write your code here
        from collections import Counter

        left, end = Counter(nums), Counter()
        for n in nums:
            if not left[n]: continue
            left[n] -= 1
            if end[n - 1] > 0:
                end[n - 1] -= 1
                end[n] += 1
            elif left[n + 1] and left[n + 2]:
                left[n + 1] -= 1
                left[n + 2] -= 1
                end[n + 2] += 1
            else:
                return False
        return True
