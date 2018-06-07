class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        # Write your code here
        return sum(1 for _ in filter(lambda x: '8' in str(x), range(1, n+1)))
