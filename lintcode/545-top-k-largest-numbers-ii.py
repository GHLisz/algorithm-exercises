import heapq


class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.min_heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.min_heap, num)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.min_heap, reverse=True)
