class Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        for i in range(len(colors)):
            while colors[i] > 0:
                num = colors[i]
                if colors[num-1] > 0:
                    colors[i] = colors[num-1]
                    colors[num-1] = -1
                elif colors[num-1] <= 0:
                    colors[num-1] -= 1
                    colors[i] = 0
        idx = len(colors) - 1
        for i in range(k-1, -1, -1):
            tmp = colors[i]
            while tmp < 0:
                colors[idx] = i + 1
                tmp += 1
                idx -= 1
