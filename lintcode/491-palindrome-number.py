class Solution:
    """
    @param: num: a positive number
    @return: true if it's a palindrome or false
    """

    def isPalindrome(self, num):
        # write your code here
        # no extra space
        length = 1
        while num // length >= 10:
            length *= 10

        while num > 0:
            left = num // length
            right = num % 10

            if left != right:
                return False
            else:
                num = (num % length) // 10
                length //= 100

        return True
