class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """

    def countPalindromicSubstrings(self, str):
        # write your code here
        def sol1():  # bf
            res, n, s = 0, len(str), str
            for i in range(n):
                j = 0
                while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                    j += 1
                    res += 1
                j = 0
                while i - 1 - j >= 0 and i + j < n and s[i - 1 - j] == s[i + j]:
                    j += 1
                    res += 1
            return res

        def sol2():  # manachers
            def manachers(S):
                A = '@#' + '#'.join(S) + '#$'
                Z = [0] * len(A)
                center = right = 0
                for i in range(1, len(A) - 1):
                    if i < right:
                        Z[i] = min(right - i, Z[2 * center - i])
                    while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                        Z[i] += 1
                    if i + Z[i] > right:
                        center, right = i, i + Z[i]
                return Z

            return sum((v + 1) / 2 for v in manachers(str))

        return sol2()
