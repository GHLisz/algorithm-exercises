class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # write your code here
        def sol1():
            res = []
            for a in arrays:
                res.extend(a)
            res.sort()
            return res

        def sol2():
            import heapq
            res, heap = [], []
            for idx, array in enumerate(arrays):
                if not array: continue
                heapq.heappush(heap, (array[0], idx, 0))
            while heap:
                val, arrayidx, idx = heapq.heappop(heap)
                res.append(val)
                if idx + 1 < len(arrays[arrayidx]):
                    heapq.heappush(heap, (arrays[arrayidx][idx + 1], arrayidx, idx + 1))
            return res

        return sol1()
