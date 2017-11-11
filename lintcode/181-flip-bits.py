class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """

    def bitSwapRequired(self, a, b):
        # write your code here
        num = a ^ b
        count = 0

        if num < 0:
            import sys
            num ^= sys.maxsize
            count += 1

        while num != 0:
            count += num % 2
            num = num // 2
        return count
