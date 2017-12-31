class Solution:
    """
    @param num: a non-negative integer N
    @return: the largest number that is less than or equal to N with monotone increasing digits.
    """

    def monotoneDigits(self, num):
        # write your code here
        s = list(str(num)[::-1])

        for i in range(len(s) - 1):
            if s[i] < s[i + 1]:
                s[i], s[i + 1] = '9', str(int(s[i + 1]) - 1)
                s[:i] = '9' * i

        return int(''.join(reversed(s)))
