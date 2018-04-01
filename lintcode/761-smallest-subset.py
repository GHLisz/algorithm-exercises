class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """
    def minElements(self, arr):
        # write your code here
        arr.sort()
        cnt, half = 0, sum(arr) // 2 + 1
        for i in range(len(arr)-1, -1, -1):
            half -= arr[i]
            cnt += 1
            if half <= 0:
                break
        return cnt
