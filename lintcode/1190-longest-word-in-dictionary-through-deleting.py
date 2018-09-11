class Solution:
    """
    @param s: a string
    @param d: List[str]
    @return: return a string
    """

    def findLongestWord(self, s, d):
        # write your code  here
        def is_subsequence(x, y):  # x is is_subsequence of y
            y = iter(y)
            return all(any(ys == xs for ys in y) for xs in x)

        max_str = ''
        for ds in d:
            if is_subsequence(ds, s):
                if len(ds) > len(max_str) or (len(ds) == len(max_str) and ds < max_str):
                    max_str = ds
        return max_str
