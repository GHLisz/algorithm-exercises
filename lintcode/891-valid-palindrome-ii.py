class Solution:
    """
    @param s: a string
    @return: nothing
    """

    def validPalindrome(self, s):
        # Write your code here
        def check(s, left, right, flag, threshold):
            while left < right:
                if s[left] == s[right]:
                    left, right = left + 1, right - 1
                else:
                    flag += 1
                    if flag > threshold: return False
                    return check(s, left + 1, right, flag, threshold) \
                           or check(s, left, right - 1, flag, threshold)
            return True

        return check(s, 0, len(s) - 1, 0, 1)
