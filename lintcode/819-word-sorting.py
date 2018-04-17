class Solution:
    """
    @param alphabet: the new alphabet
    @param words: the original string array
    @return: the string array after sorting
    """

    def wordSort(self, alphabet, words):
        # Write your code here
        rank = {}
        for i, c in enumerate(alphabet):
            rank[c] = i

        def cmp(a, b):
            for i in range(min(len(a), len(b))):
                if rank[a[i]] < rank[b[i]]:
                    return -1
                elif rank[a[i]] > rank[b[i]]:
                    return 1
            return 1 if len(a) > len(b) else -1

        from functools import cmp_to_key
        words.sort(key=cmp_to_key(cmp))
        return words
