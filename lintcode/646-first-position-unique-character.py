class Solution:
    """
    @param: s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        # write your code here
        bucket = [0 for _ in range(256)]
        for i in s:
            bucket[ord(i)] += 1
        for k, v in enumerate(s):
            if bucket[ord(v)] == 1:
                return k
        return -1
