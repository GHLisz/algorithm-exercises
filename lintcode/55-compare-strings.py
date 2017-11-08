class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here
        char_bucket = [0 for _ in range(26)]

        for i in A:
            char_bucket[ord(i) - ord('A')] += 1

        for i in B:
            if char_bucket[ord(i) - ord('A')] == 0:
                return False
            else:
                char_bucket[ord(i) - ord('A')] -= 1

        return True