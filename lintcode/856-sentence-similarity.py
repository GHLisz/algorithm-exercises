class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """

    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if len(words1) != len(words2): return False

        dic = collections.defaultdict(set)
        for k, v in pairs:
            dic[k].update([k, v])
            dic[v].update([k, v])
        for i in range(len(words1)):
            if words1[i] not in dic[words2[i]]:
                return False
        return True
