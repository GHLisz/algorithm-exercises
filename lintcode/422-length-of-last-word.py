class Solution:
    """
    @param s: A string
    @return: the length of last word
    """

    def lengthOfLastWord(self, s):
        # write your code here
        length, tail = 0, len(s) - 1

        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            length += 1
            tail -= 1

        return length
