class Solution:
    """
    @param: n: Given the range of numbers
    @param: k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        # write your code here
        def dfs(n, k, pos, temp, res):
            if k == len(temp):
                res.append(temp[:])
                return
            for i in range(pos, n + 1):
                temp.append(i)
                dfs(n, k, i + 1, temp, res)
                temp.pop()

        res = []
        dfs(n, k, 1, [], res)
        return res
