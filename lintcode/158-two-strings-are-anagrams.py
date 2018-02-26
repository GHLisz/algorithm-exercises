class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        sl = [i for i in s]
        tl = [i for i in t]
        sl.sort()
        tl.sort()
        return "".join(sl) == "".join(tl)
