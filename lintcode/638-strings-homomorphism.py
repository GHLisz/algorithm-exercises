class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """

    def isIsomorphic(self, s, t):
        # write your code here
        def sol1():
            if (not all([s, t])) or (len(s) != len(t)): return False
            n, dic1, dic2 = len(s), {}, {}
            for i in range(n):
                dic1[s[i]] = i if s[i] not in dic1 else dic1[s[i]]
                dic2[t[i]] = i if t[i] not in dic2 else dic2[t[i]]
            return [dic1[s[i]] for i in range(n)] == [dic2[t[i]] for i in range(n)]

        def sol2():
            return len(set(zip(s, t))) == len(set(s)) == len(set(t))

        def sol3():
            return list(map(s.find, s)) == list(map(t.find, t))

        return sol2()
