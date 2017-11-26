class Solution:
    """
    @param: s: a string
    @param: t: a string
    @return: true if the characters in s can be replaced to get t or false
    """

    def isIsomorphic(self, s, t):
        # write your code here
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        n = len(s)
        dic1 = {}
        dic2 = {}
        index1 = [None for _ in range(n)]
        index2 = [None for _ in range(n)]

        for i in range(n):
            if s[i] not in dic1:
                dic1[s[i]] = i
            if t[i] not in dic2:
                dic2[t[i]] = i
        for i in range(n):
            index1[i] = dic1[s[i]]
            index2[i] = dic2[t[i]]

        return index1 == index2
