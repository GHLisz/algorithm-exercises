class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    """

    def totalHammingDistance(self, nums):
        # Write your code here
        def sol1():
            total, n = 0, len(nums)
            for j in range(32):
                bit_count = sum((nums[i] >> j) & 1 for i in range(n))
                total += bit_count * (n - bit_count)
            return total

        def sol2():
            return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))

        return sol1()
