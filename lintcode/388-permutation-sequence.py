class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """

    def getPermutation(self, n, k):
        # write your code here
        from math import factorial

        elements = list(range(1, n + 1))
        ft = factorial(n)
        k, result = (k - 1) % ft, ''
        while elements:
            ft = ft // len(elements)
            i, k = divmod(k, ft)
            result += str(elements.pop(i))
        return result
