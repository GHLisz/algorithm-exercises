class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """

    def generatePalindromes(self, s):
        # write your code here
        def permute(t, start, mid, res):
            if start >= len(t):
                res.append(''.join(t) + mid + ''.join(reversed(t)))
            for i in range(start, len(t)):
                if i != start and t[i] == t[start]: continue
                t[i], t[start] = t[start], t[i]
                permute(t, start + 1, mid, res)
                t[i], t[start] = t[start], t[i]

        res, dic = [], collections.Counter(s)
        t, mid = [], ''
        for k, v in dic.items():
            if v % 2 == 1: mid += k
            t.extend([k] * (v // 2))
            if len(mid) > 1: return []
        permute(t, 0, mid, res)
        return res
