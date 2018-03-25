class Solution:
    """
    @param s: a string
    @return: nothing
    """

    def validPalindrome(self, s):
        # Write your code here
        def is_palindrome(s, left, right, flag):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if flag == 1:
                        return False
                    flag = 1
                    return is_palindrome(s, left + 1, right, flag) or \
                           is_palindrome(s, left, right - 1, flag)
            return True

        return is_palindrome(s, 0, len(s) - 1, 0)
