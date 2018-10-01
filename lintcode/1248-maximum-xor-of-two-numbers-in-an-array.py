class Solution:
    """
    @param nums:
    @return: the maximum result of ai XOR aj, where 0 ≤ i, j < n.
    """

    def findMaximumXOR(self, nums):
        # Write your code here
        mx, mask = 0, 0

        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            s = set()
            for num in nums:
                s.add(num & mask)
            tmp = mx | (1 << i)
            for prefix in s:
                if tmp ^ prefix in s:
                    mx = tmp
                    break
        return mx
