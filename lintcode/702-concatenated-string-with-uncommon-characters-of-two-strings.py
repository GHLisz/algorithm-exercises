class Solution:
    """
    @param: : the 1st string
    @param: : the 2nd string
    @return: uncommon characters of given strings
    """

    def concatenetedString(self, s1, s2):
        # write your code here
        if not s1: return s2
        if not s2: return s1

        bucket1 = [0 for _ in range(26)]
        bucket2 = [0 for _ in range(26)]

        for i in s1:
            bucket1[ord(i) - ord('a')] += 1
        for i in s2:
            bucket2[ord(i) - ord('a')] += 1

        result = ''

        for i in s1:
            if bucket2[ord(i) - ord('a')] == 0:
                result += i
        for i in s2:
            if bucket1[ord(i) - ord('a')] == 0:
                result += i

        return result
