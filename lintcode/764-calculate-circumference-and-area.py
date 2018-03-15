class Solution:
    """
    @param r: a Integer represent radius
    @return: the circle's circumference nums[0] and area nums[1]
    """
    def calculate(self, r):
        # write your code here
        PI = 3.14
        return [2 * PI * r, PI * r * r]
