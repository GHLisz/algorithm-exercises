class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """

    def characterReplacement(self, s, k):
        # write your code here
        count = [0] * 26
        start, max_count, max_length = 0, 0, 0
        for end in range(len(s)):
            count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[end]) - ord('A')])
            while end - start + 1 - max_count > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
