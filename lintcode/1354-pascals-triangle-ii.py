class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """

    def getRow(self, rowIndex):
        # write your code here
        def sol1():
            res = [[1]]
            for i in range(1, rowIndex + 1):
                res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
            return res[rowIndex]

        def sol2():
            res = [0] * (rowIndex + 1)
            res[0] = 1
            for i in range(1, rowIndex + 1):
                for j in range(i, 0, -1):
                    res[j] += res[j - 1]
            return res

        return sol2()
