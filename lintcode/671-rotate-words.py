class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """

    def countRotateWords(self, words):
        # Write your code here
        set_ = set(self.reg_word(word) for word in words)
        return len(set_)

    def reg_word(self, word):
        size = len(word)
        possibles = [(word[i:] + word[:i]) for i in range(size)]
        possibles.sort()
        return possibles[0]
