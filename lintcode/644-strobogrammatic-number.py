class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i] not in d) or (num[j] != d[num[i]]):
                return False
            i += 1
            j -= 1
        return True
