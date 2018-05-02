class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        # write your code here
        return (n*(n+1)//2) * pow(2, n-1)
