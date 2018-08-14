"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: a collection of intervals
    @return: the minimum number of intervals you need to remove
    """

    def eraseOverlapIntervals(self, intervals):
        # write your code here
        erased, end = 0, -float('inf')
        for i in sorted(intervals, key=lambda x: x.end):
            if i.start >= end:
                end = i.end
            else:
                erased += 1
        return erased
