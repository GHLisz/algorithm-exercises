class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences
    """

    def findRepeatedDna(self, s):
        # write your code here
        def encode(s):
            code = 0
            dic = {"A": 1, "C": 2, "T": 3, "G": 4, }
            for c in s:
                code <<= 2
                code += dic[c]
            return code

        res, hash = [], {}
        for i in range(10, len(s) + 1):
            substr = s[i - 10:i]
            code = encode(substr)
            if code in hash:
                if hash[code] == 1:
                    res.append(substr)
                hash[code] = 2
            else:
                hash[code] = 1
        return res
