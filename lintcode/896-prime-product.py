class Solution:
    """
    @param arr: The prime array
    @return: Return the array of all of prime product
    """

    def getPrimeProduct(self, arr):
        # Write your code here
        def dfs(ans, arr, pos, fct, cnt):
            if pos == len(arr): return
            if cnt == 0:
                dfs(ans, arr, pos + 1, fct * arr[pos], 1)
                dfs(ans, arr, pos + 1, fct, 0)
            else:
                ans.append(fct * arr[pos])
                dfs(ans, arr, pos + 1, fct * arr[pos], cnt + 1)
                dfs(ans, arr, pos + 1, fct, cnt)

        ans = []
        dfs(ans, arr, 0, 1, 0)
        ans.sort()
        return ans
