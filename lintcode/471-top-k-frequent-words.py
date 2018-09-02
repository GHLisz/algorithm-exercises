class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        # write your code here
        def sol1():  # nlogk
            import heapq, collections
            c = collections.Counter(words)
            h = [(-freq, word) for word, freq in c.items()]
            heapq.heapify(h)
            return [heapq.heappop(h)[1] for _ in range(k)]

        return sol1()
