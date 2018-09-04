"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, newInterval):
        # write your code here
        s, e = newInterval.start, newInterval.end

        parts = merge, left, right = [], [], []

        for i in intervals:
            parts[(i.end < s) - (i.start > e)].append(i)

        if merge:
            s, e = min(s, merge[0].start), max(e, merge[-1].end)

        return left + [Interval(s, e)] + right
