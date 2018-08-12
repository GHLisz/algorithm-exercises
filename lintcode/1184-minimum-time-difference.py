class Solution:
    """
    @param timePoints: a list of 24-hour clock time points
    @return: the minimum minutes difference between any two time points in the list
    """

    def findMinDifference(self, timePoints):
        # Write your code here
        minutes = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        minutes.append(minutes[0] + 24 * 60)
        return min(b - a for a, b in zip(minutes, minutes[1:]))
