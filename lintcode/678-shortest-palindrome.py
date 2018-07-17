class Solution:
    """
    @param str: String
    @return: String
    """

    def convertPalindrome(self, str):
        # Write your code here
        def sol1():  # bf
            s, rev, n = str, str[::-1], len(str)
            for i in range(n):
                if s[:n - i] == rev[i:]:
                    return rev[:i] + s
            return ''

        def sol2():  # kmp
            s, rev, n = str, str[::-1], len(str)
            s_new, n_new = s + '#' + rev, 2 * n + 1
            f = [0] * n_new
            for i in range(1, n_new):
                t = f[i - 1]
                while t > 0 and s_new[i] != s_new[t]:
                    t = f[t - 1]
                t += 1 if s_new[i] == s_new[t] else 0
                f[i] = t
            return rev[:n - f[n_new - 1]] + s

        return sol2()
