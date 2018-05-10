class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        tmp = map(lambda s: str(len(s)) + '#' + s, strs)
        return ''.join(tmp)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        s = str
        res, start = [], 0
        while start < len(s):
            idx = s.index('#', start)
            size = int(s[start:idx])
            res.append(s[idx+1:idx+size+1])
            start = idx + size + 1
        return res
