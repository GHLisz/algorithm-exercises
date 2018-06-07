class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        # write your code here
        sl, v = list(s), set('aeiouAEIOU')
        i, j = 0, len(s)-1
        while i < j:
            while sl[i] not in v and i < j:
                i += 1
            while sl[j] not in v and i < j:
                j -= 1
            sl[i], sl[j] = sl[j], sl[i]
            i += 1
            j -= 1
        return ''.join(sl)
