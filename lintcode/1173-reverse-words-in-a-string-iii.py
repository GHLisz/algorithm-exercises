class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        # Write your code here
        return ' '.join(s.split()[::-1])[::-1]
