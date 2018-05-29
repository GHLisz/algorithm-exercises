class Solution:
    """
    @param word: a string
    @return: return a boolean
    """

    def detectCapitalUse(self, word):
        # write your code here
        n = len(word)
        up = sum(1 for c in word if c.isupper())
        if up == 0 or up == n:
            return True
        if up == 1 and word[0].isupper():
            return True
        return False
