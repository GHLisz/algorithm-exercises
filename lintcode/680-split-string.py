class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if s is None:
            return []
        if len(s) == 0:
            return [[]]

        results = []
        self.dfs(results, [], 0, s)
        return results

    def dfs(self, results, result, index, s):
        if index == len(s):
            results.append(result[:])
            return

        for i in range(index, min(index + 2, len(s))):
            result.append(s[index: i + 1])
            self.dfs(results, result, i + 1, s)
            result.pop()
