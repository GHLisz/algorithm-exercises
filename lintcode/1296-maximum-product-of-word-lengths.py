class Solution:
    """
    @param words: a string array
    @return: the maximum product
    """

    def maxProduct(self, words):
        # Write your code here
        import operator
        from functools import reduce

        d = {}
        for w in words:
            mask = reduce(operator.or_, (1 << (ord(c) - ord('a')) for c in set(w)), 0)
            d[mask] = max(d.get(mask, 0), len(w))
        return max((d[x] * d[y] for x in d for y in d if not x & y), default=0)
