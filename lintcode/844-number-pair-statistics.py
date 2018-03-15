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
        for t in stat:
            ans = ans + t[0] * (t[0] - 1) / 2 + t[1] * (t[1] - 1) / 2
        return ans
