class Solution:
    """
    @param dict: List[str]
    @param sentence: a string
    @return: return a string
    """

    def replaceWords(self, roots, sentence):
        # write your code here
        from collections import defaultdict
        from functools import reduce

        Trie = lambda: defaultdict(Trie)
        trie, END = Trie(), True

        for root in roots:
            # cur = trie
            # for letter in root:
            #     cur = cur[letter]
            # cur[END] = root
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return ' '.join(map(replace, sentence.split()))
