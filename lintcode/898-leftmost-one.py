class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        # Write your code here
        ans, idx = 0, len(arr[0])-1
        for row in arr:
            while idx >= 0:
                if row[idx] == 0:
                    break
                idx -= 1
        return idx+1
