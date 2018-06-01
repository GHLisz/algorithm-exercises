class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """

    def uniqueMorseRepresentations(self, words):
        # Write your code here
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)
