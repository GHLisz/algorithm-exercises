class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, numbers):
        # Write your code here
        import heapq
        q, ans = [], 0
        for i in numbers:
            heapq.heappush(q, i)
        while len(q) > 1:
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            ans = ans + a + b
            heapq.heappush(q, a+b)
        return ans
