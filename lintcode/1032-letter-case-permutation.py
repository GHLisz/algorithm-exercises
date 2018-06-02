class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """

    def letterCasePermutation(self, S):
        # write your code here
        def sol1():
            from itertools import product
            L = [[c.lower(), c.upper()] if c.isalpha() else c for c in S]
            return sorted([''.join(i) for i in product(*L)])

        def sol2():
            res = ['']
            for ch in S:
                if ch.isalpha():
                    res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
                else:
                    res = [i + ch for i in res]
            return sorted(res)

        return sol1()
