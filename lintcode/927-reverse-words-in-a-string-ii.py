class Solution:
    """
    @param str: a string
    @return: return a string
    """

    def reverseWords(self, str):
        # write your code here
        def reverse(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1

        s, left = list(str), 0

        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                reverse(s, left, i - 1)
                left = i + 1

        reverse(s, 0, len(s) - 1)

        return ''.join(s)
