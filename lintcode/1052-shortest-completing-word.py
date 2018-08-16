class Solution:
    """
    @param licensePlate: a string
    @param words: List[str]
    @return: return a string
    """

    def shortestCompletingWord(self, licensePlate, words):
        # write your code here
        from collections import Counter
        c = Counter(filter(str.isalpha, licensePlate.lower()))
        return min((word for word in words if not c - Counter(word)), key=len)
