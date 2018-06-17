class Solution:
    """
    @param strs: a list of string
    @return: return a string
    """

    def splitLoopedString(self, strs):
        # write your code here
        if not strs: return ''

        s, res = '', 'a'
        n, cur = len(strs), 0

        for str_ in strs:
            s += max(str_, str_[::-1])

        for i in range(n):
            t1, t2 = strs[i], strs[i][::-1]
            mid = s[cur + len(t1):] + s[:cur]
            for j in range(len(strs[i])):
                if t1[j] >= res[0]:
                    res = max(res, t1[j:] + mid + t1[:j])
                if t2[j] >= res[0]:
                    res = max(res, t2[j:] + mid + t2[:j])
            cur += len(strs[i])

        return res
