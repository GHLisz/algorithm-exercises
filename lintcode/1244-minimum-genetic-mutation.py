class Solution:
    """
    @param start:
    @param end:
    @param bank:
    @return: the minimum number of mutations needed to mutate from "start" to "end"
    """

    def minMutation(self, start, end, bank):
        # Write your code here
        from collections import deque

        def is_viable_mutation(cur_mut, next_mut):
            return 1 == sum(s1 != s2 for s1, s2 in zip(cur_mut, next_mut))

        queue = deque()
        queue.append([start, start, 0])
        while queue:
            cur, prev, steps = queue.popleft()
            if cur == end:
                return steps
            for string in bank:
                if is_viable_mutation(cur, string) and string != prev:
                    queue.append([string, cur, steps + 1])
        return -1
