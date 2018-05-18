"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        time = []
        for a in airplanes:
            time.extend([(a.start, 1), (a.end, -1)])

        time.sort(key=lambda x: (x[0], x[1]))

        total, most = 0, 0
        for t, delta in time:
            total += delta
            most = max(most, total)

        return most
