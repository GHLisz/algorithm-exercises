class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """

    def calcYangHuisTriangle(self, n):
        # write your code here
        res = []
        if n == 0:
            return res

        for i in range(n):
            a = [1]
            for j in range(1, i):
                a.append(res[i - 1][j - 1] + res[i - 1][j])
            if i > 0:
                a.append(1)
            res.append(a)

        return res

