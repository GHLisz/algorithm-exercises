class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """

    def getFactors(self, n):
        # write your code here
        def helper(n, start, out, res):
            for i in range(start, int(n ** 0.5) + 1):
                if n % i: continue
                new_out = out[:]
                new_out.append(i)
                helper(n // i, i, new_out, res)
                new_out.append(n // i)
                res.append(new_out)

        res = []
        helper(n, 2, [], res)
        return res
