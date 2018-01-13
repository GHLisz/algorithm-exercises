class Solution:
    """
    @param k:
    @return: the sum of first k even-length palindrome numbers
    """
    def sumKEven(self, k):
        # Write your code here
        return sum(int(str(i)+str(i)[::-1]) for i in range(1, k+1))
