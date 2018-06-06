class Solution:
    """
    @param num: an integer
    @return: the complement number
    """

    def findComplement(self, num):
        # Write your code here
        def sol1(num):  # flip bit by bit
            i = 1
            while num >= i:
                num ^= i
                i <<= 1
            return num

        def sol2(num):
            return ~num & ((1 << num.bit_length()) - 1)

        return sol2(num)
