class Solution:
    """
    @param arr: The K spaced array
    @param k: The param k
    @return: Return the sorted array
    """
    def getSortedArray(self, arr, k):
        # Write your code here
        from queue import PriorityQueue
        ans, que = [], PriorityQueue()
        for i in range(k):
            que.put((arr[i], i))
        while not que.empty():
            head = que.get()
            ans.append(head[0])
            if head[1] + k < len(arr):
                que.put((arr[head[1] + k], head[1] + k))
        return ans
