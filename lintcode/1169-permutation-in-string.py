class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """

    def checkInclusion(self, s1, s2):
        # write your code here
        if len(s1) > len(s2): return False

        s1map, s2map = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if s1map == s2map: return True

            s2map[ord(s2[i + len(s1)]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] -= 1

        return s1map == s2map
