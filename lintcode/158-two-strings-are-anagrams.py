class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        NO_OF_CHARS = 256
        sc, tc = [0] * NO_OF_CHARS, [0] * NO_OF_CHARS
        for c in s: sc[ord(c)] += 1
        for c in t: tc[ord(c)] += 1
        return sc == tc
