class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """

    def countRotateWords(self, words):
        # Write your code here
        if not words: return 0

        count, dic = 0, set()

        for w in words:
            for i in range(len(w)):
                if w[i:] + w[:i] in dic: break
            else:
                dic.add(w)
                count += 1
        return count
