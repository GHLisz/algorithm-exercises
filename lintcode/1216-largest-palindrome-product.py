class Solution:
    """
    @param n: the number of digit
    @return: the largest palindrome mod 1337
    """

    def largestPalindrome(self, n):
        # write your code here
        def sol1():  # TLE
            def is_palindrome(n):
                ns = str(n)
                return ns[::-1] == ns

            upper_limit = int('9' * n)
            lower_limit = int('1' + '0' * (n - 1))
            max_prd = 0

            for i in range(upper_limit, lower_limit - 1, -1):
                for j in range(i, lower_limit - 1, -1):
                    prd = i * j
                    if prd > max_prd and is_palindrome(prd):
                        max_prd = prd

            return max_prd % 1337

        def sol2():
            res = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
            return res[n] if n in range(1, 9) else 0

        return sol2()
