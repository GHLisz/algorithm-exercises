class Solution:
    """
    @param area: web page's area
    @return: the length L and the width W of the web page you designed in sequence
    """

    def constructRectangle(self, area):
        # Write your code here
        l = w = int(area ** 0.5)

        while l * w != area:
            if l * w < area:
                l += 1
            else:
                w -= 1
        return [l, w]
