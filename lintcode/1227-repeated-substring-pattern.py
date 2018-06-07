class Solution:
    """
    @param s: a string
    @return: return a boolean
    """

    def repeatedSubstringPattern(self, s):
        # write your code here
        def sol1():
            if not s: return False
            return s in (s + s)[1:-1]

        def sol2():
            for i in range(1, len(s) // 2 + 1):
                if len(s) % i == 0:
                    substr = s[:i]
                    j = 0
                    while j < len(s):
                        if substr != s[j:j + len(substr)]:
                            break
                        j += len(substr)
                    if j == len(s):
                        return True
            return False

        return sol2()
