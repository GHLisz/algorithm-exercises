class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        import collections

        c = collections.Counter(str)
        return next((v for v in str if c[v] == 1), None)
