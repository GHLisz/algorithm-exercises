class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        # write your code here
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        if not str: return

        s = str
        offset = offset % len(s)
        reverse(s, 0, len(s) - offset - 1)
        reverse(s, len(s) - offset, len(s) - 1)
        reverse(s, 0, len(s) - 1)
