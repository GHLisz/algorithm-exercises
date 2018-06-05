class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """
    def canConstruct(self, ransomNote, magazine):
        # Write your code here
        from collections import Counter
        return not Counter(ransomNote) - Counter(magazine)
