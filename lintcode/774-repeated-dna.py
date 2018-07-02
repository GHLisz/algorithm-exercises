class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences
    """

    def findRepeatedDna(self, s):
        # write your code here
        def encode(s):
            code = 0
            for c in s:
                code <<= 2
                code += {"A": 1, "C": 2, "T": 3, "G": 4, }[c]
            return code

        from collections import defaultdict
        res, m = [], defaultdict(int)

        for i in range(10, len(s) + 1):
            sub = s[i - 10:i]
            code = encode(sub)
            if m[code] == 1: res.append(sub)
            m[code] += 1
        return res
