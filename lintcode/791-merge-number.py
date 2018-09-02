class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """

    def mergeNumber(self, numbers):
        # Write your code here
        import heapq

        ans = 0
        heapq.heapify(numbers)

        while len(numbers) > 1:
            a = heapq.heappop(numbers)
            b = heapq.heappop(numbers)
            ans = ans + a + b
            heapq.heappush(numbers, a + b)
        return ans
