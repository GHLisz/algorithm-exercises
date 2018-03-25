class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        bi, k = [0]*32, 0
        while n > 0:
            bi[k] = n & 1
            n >>= 1
            k += 1
        for i in range(k//2):
            if bi[i] != bi[k-i-1]:
                return False
        return True
