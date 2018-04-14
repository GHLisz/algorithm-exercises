class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """

    def canPermutePalindrome(self, s):
        # write your code here
        ct, odd = collections.Counter(s), 0
        for v in ct.values():
            if v % 2 == 1:
                odd += 1
                if odd > 1:
                    return False
        return True
