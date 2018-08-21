class Solution:
    """
    @param strs: List[str]
    @return: return an integer
    """

    def findLUSlength(self, strs):
        # write your code here
        def is_sub_seq(w1, w2):
            i = 0
            for c in w2:
                i += 1 if i < len(w1) and w1[i] == c else 0
            return i == len(w1)

        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not is_sub_seq(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1
