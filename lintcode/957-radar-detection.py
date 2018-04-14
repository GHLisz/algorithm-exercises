"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param coordinates: The radars' coordinate
    @param radius: Detection radius of radars
    @return: The car was detected or not
    """
    def radarDetection(self, coordinates, radius):
        # Write your code here
        for i in range(len(coordinates)):
            radar = coordinates[i]
            d = abs(radar.y)
            if d <= radius[i]:
                return 'YES'
        return 'NO'
