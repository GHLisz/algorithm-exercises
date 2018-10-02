"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        from collections import defaultdict

        if not intervals: return []

        m = defaultdict(int)
        for il in intervals:
            for i in il:
                m[i.start] += 1
                m[i.end] -= 1

        res, cnt = [], 0
        start, end = None, None

        for t in sorted(m.keys()):
            cnt += m[t]
            if start is None and cnt > 0:
                start = t
            if start is not None and cnt <= 0:
                end = t
                interval = Interval(start, end)
                res.append(interval)
                start = None
        return res
