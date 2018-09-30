class Solution:
    """
    @param nums: a list of integer
    @return: return a boolean
    """

    def splitArray(self, nums):
        # write your code here
        if len(nums) < 7: return False
        n, sums = len(nums), nums[:]

        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]

        for j in range(3, n - 3):
            s = set()

            for i in range(1, j - 1):
                s1 = sums[i - 1]
                s2 = sums[j - 1] - sums[i]
                if s1 == s2:
                    s.add(sums[i - 1])

            for k in range(j + 1, n - 1):
                s3 = sums[k - 1] - sums[j]
                s4 = sums[n - 1] - sums[k]
                if s3 == s4 and s3 in s:
                    return True

        return False
