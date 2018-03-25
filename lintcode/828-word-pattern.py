class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """

    def wordPattern(self, pattern, str):
        # write your code here
        slist, dic, set_ = str.split(" "), {}, set()

        if len(slist) != len(pattern):
            return False

        for i in range(len(pattern)):
            p, s = pattern[i], slist[i]
            if p in dic:
                if s != dic[p]:
                    return False
            else:
                if s in set_:
                    return False
                dic[p] = s
                set_.add(s)
        return True
