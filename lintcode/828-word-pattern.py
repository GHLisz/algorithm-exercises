class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """

    def wordPattern(self, pattern, str):
        # write your code here
        words, dic, showed = str.split(' '), {}, set()
        if len(words) != len(pattern): return False

        for i in range(len(pattern)):
            p, w = pattern[i], words[i]
            if p in dic:
                if w != dic[p]: return False
            else:
                if w in showed: return False
                dic[p] = w
                showed.add(w)
        return True
