class Solution:
    """
    @param words: a list of strings
    @return: the longest word in words that can be built one character at a time by other words in words
    """

    def longestWord(self, words):
        # Write your code here
        def sol1(words):  # near bf
            words.sort()
            words_set, longest_word = {''}, ''
            for word in words:
                if word[:-1] in words_set:
                    words_set.add(word)
                    if len(word) > len(longest_word):
                        longest_word = word
            return longest_word

        def sol2(words):  # trie
            from collections import defaultdict
            from functools import reduce

            Trie = lambda: defaultdict(Trie)
            trie = Trie()
            End = True

            for i, word in enumerate(words):
                reduce(dict.__getitem__, word, trie)[End] = i

            stack = list(trie.values())
            ans = ''
            while stack:
                cur = stack.pop()
                if End in cur:
                    word = words[cur[End]]
                    if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                        ans = word
                    stack.extend([cur[letter] for letter in cur if letter != End])
            return ans

        return sol2(words)
