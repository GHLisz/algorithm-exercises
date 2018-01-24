class Solution:
    """
    @param Matrix: the input
    @return: the element which appears every row
    """

    def FindElements(self, Matrix):
        # write your code here
        res1, res2 = set(), set()
        m, n = len(Matrix), len(Matrix[0])

        res1 = set(Matrix[0])

        for i in range(1, m):
            for j in range(n):
                val = Matrix[i][j]
                if i % 2 != 0:
                    if val in res1:
                        res2.add(val)
                else:
                    if val in res2:
                        res1.add(val)
            if i % 2 != 0:
                res1.clear()
            else:
                res2.clear()

        if m % 2 != 0:
            return res1.pop()
        else:
            return res2.pop()
