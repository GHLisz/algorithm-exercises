class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largestDivisibleSubset(self, nums):
        # write your code here
        def sol1():
            s = {-1: set()}
            for x in sorted(nums):
                s[x] = max((s[d] for d in s if x % d == 0), key=len) | {x}
            return list(max(s.values(), key=len))

        def sol2():
            n = len(nums)
            count, pre = [0] * n, [0] * n
            nums.sort()
            max_, index = 0, -1

            for i in range(n):
                count[i] = 1
                pre[i] = -1
                for j in range(i - 1, -1, -1):
                    if nums[i] % nums[j] == 0:
                        if 1 + count[j] > count[i]:
                            count[i] = count[j] + 1
                            pre[i] = j
                if count[i] > max_:
                    max_ = count[i]
                    index = i

            res = []
            while index != -1:
                res.append(nums[index])
                index = pre[index]
            return res

        return sol2()
