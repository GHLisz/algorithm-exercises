class Solution:
    """
    @param temperatures: a list of daily temperatures
    @return: a list of how many days you would have to wait until a warmer temperature
    """

    def dailyTemperatures(self, temperatures):
        # Write your code here
        ts = temperatures
        res, stack = [0] * len(ts), []
        for i in range(len(ts) - 1, -1, -1):
            while stack and ts[i] >= ts[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
