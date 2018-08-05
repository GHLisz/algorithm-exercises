class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """

    def compareVersion(self, version1, version2):
        # Write your code here
        from itertools import zip_longest
        cmp = lambda x, y: 1 if x > y else -1 if x < y else 0
        splits = (map(int, v.split('.')) for v in (version1, version2))
        return cmp(*zip(*zip_longest(*splits, fillvalue=0)))
