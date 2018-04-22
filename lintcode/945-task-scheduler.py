class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        cnt = sorted(collections.Counter(tasks).values(), reverse=True)
        mx, mx_cnt = cnt[0], cnt.count(cnt[0])
        return max(len(tasks), (mx-1)*(n+1)+mx_cnt)
