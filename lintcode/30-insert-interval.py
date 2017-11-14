"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        result = []
        insert_idx = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                result.append(interval)
                insert_idx += 1
            elif interval.start > newInterval.end:
                result.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        result.insert(insert_idx, newInterval)
        return result

