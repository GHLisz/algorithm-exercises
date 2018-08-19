class Solution:
    """
    @param arr: an array of integers
    @return: number of chunks
    """

    def maxChunksToSorted(self, arr):
        # Write your code here
        def sol1():  # sliding window
            from collections import defaultdict

            ans, nonzero, count = 0, 0, defaultdict(int)
            for x, y in zip(arr, sorted(arr)):
                count[x] += 1
                if count[x] == 0: nonzero -= 1
                if count[x] == 1: nonzero += 1

                count[y] -= 1
                if count[y] == -1: nonzero += 1
                if count[y] == 0: nonzero -= 1

                if nonzero == 0: ans += 1
            return ans

        def sol2():  # linear time
            from itertools import accumulate

            max_of_left = list(accumulate(arr, max))
            min_of_right = list(accumulate(arr[::-1], min))[::-1]
            return sum(1 for i in range(len(arr) - 1) if max_of_left[i] <= min_of_right[i + 1]) + 1

        return sol2()
