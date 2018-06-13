class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """

    def killProcess(self, pid, ppid, kill):
        # Write your code here
        from collections import defaultdict

        res, kill_queue, m = [], [kill], defaultdict(list)

        for i in range(len(pid)):
            m[ppid[i]].append(pid[i])

        while kill_queue:
            t = kill_queue.pop(0)
            res.append(t)
            for p in m[t]:
                kill_queue.append(p)

        return res
