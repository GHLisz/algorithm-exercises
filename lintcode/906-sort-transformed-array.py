class Solution:
    """
    @param nums: a sorted array
    @param a:
    @param b:
    @param c:
    @return: a sorted array
    """

    def sortTransformedArray(self, nums, a, b, c):
        # Write your code here
        def f(x):
            return a * x * x + b * x + c

        n = len(nums)
        i, j = 0, n - 1
        res = [0] * n
        idx = n - 1 if a >= 0 else 0

        while i <= j:
            fi, fj = f(nums[i]), f(nums[j])
            if a >= 0:
                if fi >= fj:
                    res[idx] = fi
                    i += 1
                else:
                    res[idx] = fj
                    j -= 1
                idx -= 1
            else:
                if fi >= fj:
                    res[idx] = fj
                    j -= 1
                else:
                    res[idx] = fi
                    i += 1
                idx += 1
        return res
