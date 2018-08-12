class Solution:
    """
    @param nums: an array
    @return: whether you could make one square using all the matchsticks the little match girl has
    """

    def makesquare(self, nums):
        # Write your code here
        def dfs(lefts, idx, nums):
            if idx == len(nums): return True
            n, used = nums[idx], set()
            for i, left in enumerate(lefts):
                if left >= n and left not in used:
                    lefts[i] -= n
                    if dfs(lefts, idx + 1, nums): return True
                    lefts[i] += n
                    used.add(left)
            return False

        total, target = sum(nums), sum(nums) // 4
        if len(nums) < 4 or total % 4 or any(n > target for n in nums): return False
        nums.sort(reverse=True)
        return dfs([target] * 4, 0, nums)
