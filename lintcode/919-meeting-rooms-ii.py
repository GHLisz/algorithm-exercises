"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        dic = collections.defaultdict(int)
        for a in intervals:
            dic[a.start] += 1
            dic[a.end] -= 1
        rooms, res = 0, 0
        for k, v in sorted(dic.items(), key=lambda x: x[0]):
            rooms += v
            res = max(res, rooms)
        return res
