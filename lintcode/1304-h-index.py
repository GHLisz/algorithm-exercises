class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """

    def hIndex(self, citations):
        # write your code here
        def sol1():
            citations.sort()
            n = len(citations)
            for i in range(n):
                if citations[i] >= n - i:
                    return n - i
            return 0

        def sol2():
            n = len(citations)

            cite_count = [0] * (n + 1)
            for c in citations:
                if c >= n:
                    cite_count[n] += 1
                else:
                    cite_count[c] += 1

            i = n - 1
            while i >= 0:
                cite_count[i] += cite_count[i + 1]
                if cite_count[i + 1] >= i + 1:
                    return i + 1
                i -= 1
            return 0

        return sol2()
