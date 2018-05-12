class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    def pairNumbers(self, p):
        # Write your code here
        stat = [[0, 0], [0, 0]]
        for v in p:
            stat[v.x % 2][v.y % 2] += 1
        ans = 0
        for lis in stat:
            for n in lis:
                ans += n * (n-1) / 2
        return ans
