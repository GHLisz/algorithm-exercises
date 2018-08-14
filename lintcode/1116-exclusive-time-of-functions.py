class Solution:
    """
    @param n: a integer
    @param logs: a list of integers
    @return: return a list of integers
    """

    def exclusiveTime(self, n, logs):
        # write your code here
        res, stack = [0] * n, []
        for log in logs:
            fid, status, time = map(int, log.replace('start', '1').replace('end', '0').split(':'))
            if status:
                stack.append([time, 0])
            else:
                start, inner_time = stack.pop()
                res[fid] += time - start + 1 - inner_time
                if stack:
                    stack[-1][-1] += time - start + 1
        return res
