class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """

    def twitchWords(self, str):
        # Write your code here
        res, s = [], str

        i = 0
        while i < len(s) - 2:
            if s[i] == s[i + 1] == s[i + 2]:
                j = i + 3
                while j < len(s):
                    if s[j] != s[i]: break
                    j += 1
                res.append([i, j - 1])

                i = j
            else:
                i += 1
        return res
