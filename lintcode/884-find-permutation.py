class Solution:
    """
    @param s: a string
    @return: return a list of integers
    """
    def findPermutation(self, s):
        # write your code here
        def sol1():
            res, i = [1] * (len(s) + 1), 1
            while i <= len(s):
                res[i], j = i + 1, i
                if s[i - 1] == 'D':
                    while i <= len(s) and s[i - 1] == 'D':
                        i += 1
                    k, c = j - 1, i
                    while k <= i - 1:
                        res[k] = c
                        k += 1
                        c -= 1
                else:
                    i += 1
            return res

        def sol2():
            def reverse(a, start, end):
                for i in range((end - start) // 2):
                    a[end - i - 1], a[start + i] = a[start + i], a[end - i - 1]

            res, i = list(range(1, len(s) + 2)), 1
            while i <= len(s):
                j = i
                while i <= len(s) and s[i - 1] == 'D':
                    i += 1
                reverse(res, j - 1, i)
                i += 1
            return res

        return sol2()