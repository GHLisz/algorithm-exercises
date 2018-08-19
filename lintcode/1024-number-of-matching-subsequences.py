class Solution:
    """
    @param S: a string
    @param words: a dictionary of words
    @return: the number of words[i] that is a subsequence of S
    """

    def numMatchingSubseq(self, S, words):
        # Write your code here
        from collections import defaultdict

        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])
