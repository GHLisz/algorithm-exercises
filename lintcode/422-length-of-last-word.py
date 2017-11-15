class Solution:
    """
    @param: s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        # write your code here
        if not s:
            return 0
        last_word = s.split()[-1]
        return len(last_word)
