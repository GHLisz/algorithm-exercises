class Solution:
    """
    @param bits: a array represented by several bits.
    @return: whether the last character must be a one-bit character or not
    """

    def isOneBitCharacter(self, bits):
        # Write your code here
        def sol1():
            i = 0
            while i < len(bits) - 1:
                if bits[i] == 0:
                    i += 1
                elif bits[i] == 1:
                    i += 2
            return i == len(bits) - 1

        def sol2():  # greedy
            i = len(bits) - 2
            while i >= 0 and bits[i] > 0:
                i -= 1
            return (len(bits) - i) % 2 == 0

        return sol2()
