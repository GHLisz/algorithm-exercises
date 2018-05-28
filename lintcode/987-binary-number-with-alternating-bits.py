class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits(self, n):
        # Write your code here
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits)-1))
