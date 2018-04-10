class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, str):
        # write your code here
        if len(str) < 3:
            return str

        s, res = str, ''
        this_char, this_cnt = s[0], 1
        res += this_char
        for i in range(1, len(s)):
            if s[i] == this_char:
                this_cnt += 1
            else:
                res += repr(this_cnt)
                this_char = s[i]
                this_cnt = 1
                res += this_char
        res += repr(this_cnt)
        return res if len(res) < len(s) else s
