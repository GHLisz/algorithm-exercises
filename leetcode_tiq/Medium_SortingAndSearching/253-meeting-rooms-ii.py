"""
253. Meeting Rooms II
Medium

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example
Given intervals = [(0,30),(5,10),(15,20)], return 2.
"""


# Definition of Interval.
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        from collections import defaultdict

        d = defaultdict(int)
        for i in intervals:
            d[i.start] += 1
            d[i.end] -= 1

        rooms, res = 0, 0
        for k, v in sorted(d.items(), key=lambda x: x[0]):
            rooms += v
            res = max(res, rooms)

        return res
