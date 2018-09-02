class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """

    def majorityNumber(self, nums, k):
        # write your code here
        from collections import Counter

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
            if len(cnt) >= k:
                cnt = {k: v - 1 for k, v in cnt.items() if v - 1}

        cnt = Counter(n for n in nums if n in cnt.keys())
        return next(k for k, v in cnt.items() if v == max(cnt.values()))
