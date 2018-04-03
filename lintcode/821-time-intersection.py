"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    def timeIntersection(self, seqA, seqB):
        # Write your code here
        visit = [0] * 1000001
        for i in seqA:
            for j in range(i.start, i.end + 1):
                visit[j] += 1
        for i in seqB:
            for j in range(i.start, i.end + 1):
                visit[j] += 1

        ans, i = [], 0
        while i < 1000001:
            if visit[i] == 2:
                tmp = Interval(0, 0)
                tmp.start = i
                for j in range(i, 1000001):
                    if visit[j] != 2:
                        tmp.end = j - 1
                        break
                ans.append(tmp)
                i = tmp.end
            i += 1
        return ans
