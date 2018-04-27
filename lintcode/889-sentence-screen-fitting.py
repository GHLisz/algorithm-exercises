class Solution:
    """
    @param sentence: a list of string
    @param rows: an integer
    @param cols: an integer
    @return: return an integer, denote times the given sentence can be fitted on the screen
    """
    def wordsTyping(self, sentence, rows, cols):
        # Write your code here
        s = ' '.join(sentence) + ' '
        start, n = 0, len(s)
        for i in range(rows):
            start += cols
            if s[start % n] == ' ':
                start += 1
                continue
            while start > 0 and s[(start-1) % n] != ' ':
                start -= 1
        return start // n
