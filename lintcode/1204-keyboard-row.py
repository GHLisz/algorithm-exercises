class Solution:
    """
    @param words: a list of strings
    @return: return a list of strings
    """
    def findWords(self, words):
        # write your code here
        def in_one_line(word):
            line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
            w = set(word.lower())
            return any(map(lambda x: w.issubset(x), [line1, line2, line3]))

        return list(filter(lambda w: in_one_line(w), words))
